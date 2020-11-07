from .cql_parser import CorpusQLParser, CorpusQLVisitor
from typing import List, Dict

Token = Dict[str, str]
class CqlQuery(CorpusQLVisitor):
    def __init__(self, tokens: List[Token]):
        pass
    
    # Visit a parse tree produced by CorpusQLParser#query.
    def visitQuery(self, ctx:CorpusQLParser.QueryContext):
        print("visitQuery", ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#complexQuery.
    def visitComplexQuery(self, ctx:CorpusQLParser.ComplexQueryContext):
        print("visitComplexQuery", ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#within.
    def visitWithin(self, ctx:CorpusQLParser.WithinContext):
        raise NotImplementedError("WITHIN keyword is not implemented")

    # Visit a parse tree produced by CorpusQLParser#containing.
    def visitContaining(self, ctx:CorpusQLParser.ContainingContext):
        raise NotImplementedError("CONTAINING keyword is not implemented")

    # Visit a parse tree produced by CorpusQLParser#simpleQuery.
    def visitSimpleQuery(self, ctx:CorpusQLParser.SimpleQueryContext):
        print("visitSimpleQuery")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#sequence.
    def visitSequence(self, ctx:CorpusQLParser.SequenceContext):
        print("visitSequence")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#sequencePart.
    def visitSequencePart(self, ctx:CorpusQLParser.SequencePartContext):
        print("visitSequencePart")
        for child in ctx.children:
            print("visit child: ", child.__class__.__name__)
            self.visit(child)
        return None


    # Visit a parse tree produced by CorpusQLParser#tag.
    def visitTag(self, ctx:CorpusQLParser.TagContext):
        print("visitTag")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#attribute.
    def visitAttribute(self, ctx:CorpusQLParser.AttributeContext):
        print("visitAttribute")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#positionPositionWord.
    def visitPositionPositionWord(self, ctx:CorpusQLParser.PositionPositionWordContext):
        print("visitPositionPositionWord")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#positionPositionLong.
    def visitPositionPositionLong(self, ctx:CorpusQLParser.PositionPositionLongContext):
        print("visitPositionPositionLong")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#positionWord.
    def visitPositionWord(self, ctx:CorpusQLParser.PositionWordContext):
        print("visitPositionWord")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#positionLong.
    def visitPositionLong(self, ctx:CorpusQLParser.PositionLongContext):
        print("visitPositionLong")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#positionLongPart.
    def visitPositionLongPart(self, ctx:CorpusQLParser.PositionLongPartContext):
        print("visitPositionLongPart")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#attValuePairEquals.
    def visitAttValuePairEquals(self, ctx:CorpusQLParser.AttValuePairEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#attValuePairNotEquals.
    def visitAttValuePairNotEquals(self, ctx:CorpusQLParser.AttValuePairNotEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#attValuePairDefaultEquals.
    def visitAttValuePairDefaultEquals(self, ctx:CorpusQLParser.AttValuePairDefaultEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#propName.
    def visitPropName(self, ctx:CorpusQLParser.PropNameContext):
        print("visitPropName")
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
        print("visitQuotedString")
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
        print("visitValuePartString")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#valuePartParenthesised.
    def visitValuePartParenthesised(self, ctx:CorpusQLParser.ValuePartParenthesisedContext):
        print("visitValuePartParenthesised")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#valueWith.
    def visitValueWith(self, ctx:CorpusQLParser.ValueWithContext):
        print("visitValueWith")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#valueWithout.
    def visitValueWithout(self, ctx:CorpusQLParser.ValueWithoutContext):
        print("visitValueWithout")
        return self.visitChildren(ctx)