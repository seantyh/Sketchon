# Generated from ../src/sketchon/cql_parser/CorpusQL.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CorpusQLParser import CorpusQLParser
else:
    from CorpusQLParser import CorpusQLParser

# This class defines a complete generic visitor for a parse tree produced by CorpusQLParser.

class CorpusQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CorpusQLParser#query.
    def visitQuery(self, ctx:CorpusQLParser.QueryContext):
        return self.visitChildren(ctx)


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


    # Visit a parse tree produced by CorpusQLParser#positionLongPartAttValuePair.
    def visitPositionLongPartAttValuePair(self, ctx:CorpusQLParser.PositionLongPartAttValuePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#positionLongPartParenthesised.
    def visitPositionLongPartParenthesised(self, ctx:CorpusQLParser.PositionLongPartParenthesisedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#positionLongPartNegated.
    def visitPositionLongPartNegated(self, ctx:CorpusQLParser.PositionLongPartNegatedContext):
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#valuePartParenthesised.
    def visitValuePartParenthesised(self, ctx:CorpusQLParser.ValuePartParenthesisedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#valueWith.
    def visitValueWith(self, ctx:CorpusQLParser.ValueWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusQLParser#valueWithout.
    def visitValueWithout(self, ctx:CorpusQLParser.ValueWithoutContext):
        return self.visitChildren(ctx)



del CorpusQLParser