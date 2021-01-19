import re
from .cql_parser import CorpusQLVisitor, CorpusQLParser
from .cql_parser import CorpusQLParser as cqlp

class CqlMatcher(CorpusQLVisitor):

    def __init__(self, tokens, token_default={}):
        self.results = {}
        self.states = {}
        self.__cursor = 0
        self.intokens = tokens 
        self.selected_propName = None        
        self.token_default = token_default      

    @property
    def cursor(self):
        return self.__cursor

    def set_cursor(self, new_cursor_pos):
        self.__cursor = new_cursor_pos

    def get_token_value(self, cursor=None, propName=None):
        if not cursor:
            cursor = self.cursor

        if not propName:
            propName = "word"

        if 0 <= cursor < len(self.intokens):
            return getattr(self.intokens[cursor], propName, "")
        else:
            return ""

    # Visit a parse tree produced by CorpusQLParser#query.
    def visitQuery(self, ctx:CorpusQLParser.QueryContext):
        result = self.visitChildren(ctx)
        return result


    # Visit a parse tree produced by CorpusQLParser#complexQuery.
    def visitComplexQuery(self, ctx:CorpusQLParser.ComplexQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#within.
    def visitWithin(self, ctx:CorpusQLParser.WithinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#containing.
    def visitContaining(self, ctx:CorpusQLParser.ContainingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#simpleQuery.
    def visitSimpleQuery(self, ctx:CorpusQLParser.SimpleQueryContext):        
        seqCtx = ctx.getChild(0)
        matchA = self.visit(seqCtx)
        start = matchA[0]["range"][0]
        if ctx.getChildCount() > 1:
            # has boolean operator
            boolOp = ctx.getChild(1).getText()
            queryCtx = ctx.getChild(3)
            matchB = self.visit(queryCtx)
            end = 0
            
            matchA_end = matchA[-1]["range"][1]
            matchB_end = matchB[-1]["range"][1]
            if boolOp == "|":
                end = max(matchA_end, matchB_end)
            elif boolOp == "&" and matchA_end == matchB_end:
                end = matchA_end
            else:
                raise NotImplementedError("boolean operator not implemented: ", boolOp)
            mrange = (start, end)        
        else:        
            # only longPartRule    
            mrange = matchA
        return mrange


    # Visit a parse tree produced by CorpusQLParser#sequence.
    def visitSequence(self, ctx:CorpusQLParser.SequenceContext):
        seq_matches = []
        for seq_x in ctx.getChildren():
            seq_matches.append(seq_matches)
        return seq_matches


    # Visit a parse tree produced by CorpusQLParser#sequencePart.
    def visitSequencePart(self, ctx:CorpusQLParser.SequencePartContext):        
        print("sequencePart: ", ctx.getChildCount())        
        # get quant        
        quantCtx = ctx.getTypedRuleContext(cqlp.RepetitionAmountContext, 0)
        if quantCtx:
            self.visit(quantCtx)
        quant = getattr(ctx, "quant", (1,1))                

        if not quant[1]: # if upper limit is not set
            quant[1] = 1e5 # set an arbitrary large integer

        # find label
        if ctx.getChild(1) == ':':
            seqLabel = ctx.getChild(0).getText()
            print("sequenceLabel", seqLabel)
        else:
            seqLabel = ""

        targetCtx = None
        targetCtx = ctx.getTypedRuleContext(cqlp.ComplexQueryContext, 0)
        targetCtx = targetCtx or ctx.getTypedRuleContext(cqlp.PositionContext, 0)
        
        # begin matching
        old_cursor = self.cursor
        mrange_list = []
        mrange = self.visit(targetCtx)        
        while mrange[0] == mrange[1]:
            mrange_list.append(mrange)

            # if already reach the upper limit
            if len(mrange_list) >= quant[1]:
                break
            self.set_cursor(self.cursor+1)
            mrange = self.visit(targetCtx)            


        ret_range = (self.cursor, self.cursor)
        # check quantifiers
        if quant[0] <= len(mrange_list) <= quant[1]:
            ret_range = (mrange_list[0][0], mrange_list[-1][1])
            self.set_cursor(mrange[-1][1])
        else:
            # reset the cursor
            self.set_cursor(old_cursor)
            ret_range = (self.cursor, self.cursor)

        return {"range": ret_range, "label": seqLabel}

    # Visit a parse tree produced by CorpusQLParser#repetitionExactly.
    def visitRepetitionExactly(self, ctx:CorpusQLParser.RepetitionExactlyContext):
        lb = int(ctx.getChild(1).getText())
        setattr(ctx.parentCtx, "quant", (lb, lb))
        return None


    # Visit a parse tree produced by CorpusQLParser#repetitionMinMax.
    def visitRepetitionMinMax(self, ctx:CorpusQLParser.RepetitionMinMaxContext):
        lb = int(ctx.getChild(1).getText())
        if ctx.getChildCount() > 3:
            ub = int(ctx.getChild(3).getText())
        else:
            ub = None
        setattr(ctx.parentCtx, "quant", (lb, ub))
        return None

    # Visit a parse tree produced by CorpusQLParser#positionPositionWord.
    def visitPositionPositionWord(self, ctx:CorpusQLParser.PositionPositionWordContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by CorpusQLParser#positionPositionLong.
    def visitPositionPositionLong(self, ctx:CorpusQLParser.PositionPositionLongContext):
        if ctx.getChildCount() > 2:
            return self.visit(ctx.getChild(1))
        else:
            return (self.cursor, self.cusor+1)


    # Visit a parse tree produced by CorpusQLParser#positionWord.
    def visitPositionWord(self, ctx:CorpusQLParser.PositionWordContext):
        qsCtx = ctx.getTypedRuleContext(cqlp.QuotedStringContext, 0)
        qs = self.visit(qsCtx)
        tokenValue = self.get_token_value()
        if re.match(qs, tokenValue):
            return (self.cursor, self.cursor+1)
        else:
            return (self.cursor, self.cursor)

    # Visit a parse tree produced by CorpusQLParser#positionLong.
    def visitPositionLong(self, ctx:CorpusQLParser.PositionLongContext):
        longPartCtx = ctx.getChild(0)
        matchA = self.visit(longPartCtx)
        if ctx.getChildCount() > 1:
            # has boolean operator
            boolOp = ctx.getChild(1).getText()
            longCtx = ctx.getChild(2)
            matchB = self.visit(longCtx)
            end = 0
            if boolOp == "|":
                end = max(matchA[1], matchB[1])
            elif boolOp == "&":
                end = min(matchA[1], matchB[1])
            else:
                raise NotImplementedError("boolean operator not implemented: ", boolOp)
            mrange = (matchA[0], end)        
        else:        
            # only longPartRule    
            mrange = matchA
        return mrange

    # Visit a parse tree produced by CorpusQLParser#positionLongPartAttValuePair.
    def visitPositionLongPartAttValuePair(self, ctx:CorpusQLParser.PositionLongPartAttValuePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#positionLongPartParenthesised.
    def visitPositionLongPartParenthesised(self, ctx:CorpusQLParser.PositionLongPartParenthesisedContext):
        longPartCtx = ctx.getTypedRuleContext(cqlp.PositionLongContext, 0)
        return self.visit(longPartCtx)


    # Visit a parse tree produced by CorpusQLParser#positionLongPartNegated.
    def visitPositionLongPartNegated(self, ctx:CorpusQLParser.PositionLongPartNegatedContext):
        longPartCtx = ctx.getTypedRuleContext(cqlp.PositionLongPartContext, 0)
        mrange = self.visit(longPartCtx)
        if mrange[0] != mrange[1]:
            # matched
            return (mrange[0], mrange[0])
        else:
            # not matched
            return (mrange[0], mrange[1])        


    # Visit a parse tree produced by CorpusQLParser#attValuePairDefaultEquals.
    def visitAttValuePairEquals(self, ctx:CorpusQLParser.AttValuePairContext):
        print("visitAttValuePair")
        propCtx = ctx.getTypedRuleContext(cqlp.PropNameContext, 0)
        valuePartsCtx = ctx.getTypedRuleContext(cqlp.ValuePartContext, 0)
        prop = self.visit(propCtx)
        self.selected_propName = prop
        return self.visit(valuePartsCtx)


    # Visit a parse tree produced by CorpusQLParser#attValuePairNotEquals.
    def visitAttValuePairNotEquals(self, ctx:CorpusQLParser.AttValuePairNotEqualsContext):        
        propCtx = ctx.getTypedRuleContext(cqlp.PropNameContext, 0)
        valuePartsCtx = ctx.getTypedRuleContext(cqlp.ValuePartContext, 0)
        prop = self.visit(propCtx)
        self.selected_propName = prop
        mrange = self.visit(valuePartsCtx)
        # negate matched pattern:
        if mrange[1] - mrange[0] == 0:
            # matched -> not matched
            return (mrange[0], mrange[0])
        else:
            # not matched -> matched
            return (mrange[0], mrange[0]+1)



    # Visit a parse tree produced by CorpusQLParser#attValuePairDefaultEquals.
    def visitAttValuePairDefaultEquals(self, ctx:CorpusQLParser.AttValuePairDefaultEqualsContext):
        propCtx = ctx.getTypedRuleContext(cqlp.PropNameContext, 0)
        valuePartsCtx = ctx.getTypedRuleContext(cqlp.ValuePartContext, 0)
        prop = self.visit(propCtx)
        self.selected_propName = None  # use default vaule in get_token_value()
        return self.visit(valuePartsCtx)


    # Visit a parse tree produced by CorpusQLParser#propName.
    def visitPropName(self, ctx:CorpusQLParser.PropNameContext):
        return ctx.getText()


    # Visit a parse tree produced by CorpusQLParser#quotedString.
    def visitQuotedString(self, ctx:CorpusQLParser.QuotedStringContext):
        qs = ctx.getText()
        if qs:
            return qs[1:-1]  # read content within quotes
        else:
            return ""  # qs is an empty string                   


    # Visit a parse tree produced by CorpusQLParser#valuePartString.
    def visitValuePartString(self, ctx:CorpusQLParser.ValuePartStringContext):
        start = self.cursor   
        qsCtx = ctx.getTypedRuleContext(cqlp.QuotedStringContext, 0)             
        tokenValue = self.get_token_value(self.cursor, self.selected_propName)        
        qs = self.visit(qsCtx)
        if re.match(qs, tokenValue):
            return (self.cursor, self.cursor+1)
        else:
            return (self.cursor, self.cursor)        


    # Visit a parse tree produced by CorpusQLParser#valuePartParenthesised.
    def visitValuePartParenthesised(self, ctx:CorpusQLParser.ValuePartParenthesisedContext):
        valueCtx = ctx.getTypedRuleContext(cqlp.ValueContext, 0)
        (start, end) = self.visit(valueCtx)                
        return (start, end)

    # Visit a parse tree produced by CorpusQLParser#valueWith.
    def visitValueWith(self, ctx:CorpusQLParser.ValueWithContext):
        start = self.cursor
        boolCtx = ctx.getTypedRuleContext(cqlp.BooleanOperatorContext, 0)
        boolOp = boolCtx.getText()
        ctxA = ctx.getTypedRuleContext(cqlp.ValuePartContext, 0)
        ctxB = ctx.getTypedRuleContext(cqlp.ValueContext, 0)
        matchA = self.visit(ctxA)
        matchB = self.visit(ctxB)
        print(matchA, matchB)

        if boolOp == "|":
            end = max(matchA[1], matchB[1])
        elif boolOp == "&":
            end = min(matchA[1], matchB[1])
        else:
            raise NotImplementedError("boolean operator not implemented: ", boolCtx)
        return (start, end)
        
    # Visit a parse tree produced by CorpusQLParser#valueWithout.
    def visitValueWithout(self, ctx:CorpusQLParser.ValueWithoutContext):
        valuePartCtx = ctx.getTypedRuleContext(cqlp.ValuePartContext, 0)
        return self.visit(valuePartCtx)



del CorpusQLParser