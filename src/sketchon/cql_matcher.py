import re
from .cql_parser import CorpusQLVisitor, CorpusQLParser
from .cql_parser import CorpusQLParser as cqlp

class CqlMatcher(CorpusQLVisitor):

    def __init__(self, tokens, token_default={}):
        self.results = {}
        self.states = {}
        self.__cursor = 0
        self.intokens = tokens
        self.attr_func = lambda x: x.word  
        self.token_default = token_default      

    @property
    def cursor(self):
        return self.__cursor
    
    def set_attr_func(self, attrName):
        self.attr_func = lambda x: getattr(x, attrName, "")

    def reset_attr_func(self):
        self.attr_func = lambda x: x.word

    def set_cursor(self, new_cursor_pos):
        self.__cursor = new_cursor_pos

    def get_token(self, cursor):
        if 0 <= cursor < len(self.intokens):
            return self.intokens[cursor]
        else:
            return self.token_default

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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#sequence.
    def visitSequence(self, ctx:CorpusQLParser.SequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#sequencePart.
    def visitSequencePart(self, ctx:CorpusQLParser.SequencePartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#tag.
    def visitTag(self, ctx:CorpusQLParser.TagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#attribute.
    def visitAttribute(self, ctx:CorpusQLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#positionPositionWord.
    def visitPositionPositionWord(self, ctx:CorpusQLParser.PositionPositionWordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#positionPositionLong.
    def visitPositionPositionLong(self, ctx:CorpusQLParser.PositionPositionLongContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#positionWord.
    def visitPositionWord(self, ctx:CorpusQLParser.PositionWordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#positionLong.
    def visitPositionLong(self, ctx:CorpusQLParser.PositionLongContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#positionLongPart.
    def visitPositionLongPart(self, ctx:CorpusQLParser.PositionLongPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#attValuePairEquals.
    def visitAttValuePairEquals(self, ctx:CorpusQLParser.AttValuePairEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#attValuePairNotEquals.
    def visitAttValuePairNotEquals(self, ctx:CorpusQLParser.AttValuePairNotEqualsContext):
        results = self.visitChildren(ctx)
        token = (None, None, results["valuePart"])        
        return token

    # Visit a parse tree produced by CorpusQLParser#attValuePairDefaultEquals.
    def visitAttValuePairDefaultEquals(self, ctx:CorpusQLParser.AttValuePairDefaultEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#propName.
    def visitPropName(self, ctx:CorpusQLParser.PropNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#repetitionZeroOrMore.
    def visitRepetitionZeroOrMore(self, ctx:CorpusQLParser.RepetitionZeroOrMoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#repetitionOneOrMore.
    def visitRepetitionOneOrMore(self, ctx:CorpusQLParser.RepetitionOneOrMoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#repetitionZeroOrOne.
    def visitRepetitionZeroOrOne(self, ctx:CorpusQLParser.RepetitionZeroOrOneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#repetitionExactly.
    def visitRepetitionExactly(self, ctx:CorpusQLParser.RepetitionExactlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#repetitionMinMax.
    def visitRepetitionMinMax(self, ctx:CorpusQLParser.RepetitionMinMaxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#quotedString.
    def visitQuotedString(self, ctx:CorpusQLParser.QuotedStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#and.
    def visitAnd(self, ctx:CorpusQLParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#or.
    def visitOr(self, ctx:CorpusQLParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#implication.
    def visitImplication(self, ctx:CorpusQLParser.ImplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#valuePartString.
    def visitValuePartString(self, ctx:CorpusQLParser.ValuePartStringContext):
        start = self.cursor        
        quotedText = ctx.getChild(0).getText()[1:-1]     
        mat = re.match(quotedText, self.attr_func(self.get_token(start)))
        if mat:
            end = start + 1
        else:
            end = start
        return (start, end)


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