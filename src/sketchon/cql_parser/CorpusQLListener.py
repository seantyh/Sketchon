# Generated from ../src/sketchon/cql_parser/CorpusQL.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CorpusQLParser import CorpusQLParser
else:
    from CorpusQLParser import CorpusQLParser

# This class defines a complete listener for a parse tree produced by CorpusQLParser.
class CorpusQLListener(ParseTreeListener):

    # Enter a parse tree produced by CorpusQLParser#query.
    def enterQuery(self, ctx:CorpusQLParser.QueryContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#query.
    def exitQuery(self, ctx:CorpusQLParser.QueryContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#complexQuery.
    def enterComplexQuery(self, ctx:CorpusQLParser.ComplexQueryContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#complexQuery.
    def exitComplexQuery(self, ctx:CorpusQLParser.ComplexQueryContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#within.
    def enterWithin(self, ctx:CorpusQLParser.WithinContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#within.
    def exitWithin(self, ctx:CorpusQLParser.WithinContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#containing.
    def enterContaining(self, ctx:CorpusQLParser.ContainingContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#containing.
    def exitContaining(self, ctx:CorpusQLParser.ContainingContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#simpleQuery.
    def enterSimpleQuery(self, ctx:CorpusQLParser.SimpleQueryContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#simpleQuery.
    def exitSimpleQuery(self, ctx:CorpusQLParser.SimpleQueryContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#sequence.
    def enterSequence(self, ctx:CorpusQLParser.SequenceContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#sequence.
    def exitSequence(self, ctx:CorpusQLParser.SequenceContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#sequencePart.
    def enterSequencePart(self, ctx:CorpusQLParser.SequencePartContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#sequencePart.
    def exitSequencePart(self, ctx:CorpusQLParser.SequencePartContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#tag.
    def enterTag(self, ctx:CorpusQLParser.TagContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#tag.
    def exitTag(self, ctx:CorpusQLParser.TagContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#attribute.
    def enterAttribute(self, ctx:CorpusQLParser.AttributeContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#attribute.
    def exitAttribute(self, ctx:CorpusQLParser.AttributeContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#positionPositionWord.
    def enterPositionPositionWord(self, ctx:CorpusQLParser.PositionPositionWordContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#positionPositionWord.
    def exitPositionPositionWord(self, ctx:CorpusQLParser.PositionPositionWordContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#positionPositionLong.
    def enterPositionPositionLong(self, ctx:CorpusQLParser.PositionPositionLongContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#positionPositionLong.
    def exitPositionPositionLong(self, ctx:CorpusQLParser.PositionPositionLongContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#positionWord.
    def enterPositionWord(self, ctx:CorpusQLParser.PositionWordContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#positionWord.
    def exitPositionWord(self, ctx:CorpusQLParser.PositionWordContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#positionLong.
    def enterPositionLong(self, ctx:CorpusQLParser.PositionLongContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#positionLong.
    def exitPositionLong(self, ctx:CorpusQLParser.PositionLongContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#positionLongPart.
    def enterPositionLongPart(self, ctx:CorpusQLParser.PositionLongPartContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#positionLongPart.
    def exitPositionLongPart(self, ctx:CorpusQLParser.PositionLongPartContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#attValuePairEquals.
    def enterAttValuePairEquals(self, ctx:CorpusQLParser.AttValuePairEqualsContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#attValuePairEquals.
    def exitAttValuePairEquals(self, ctx:CorpusQLParser.AttValuePairEqualsContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#attValuePairNotEquals.
    def enterAttValuePairNotEquals(self, ctx:CorpusQLParser.AttValuePairNotEqualsContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#attValuePairNotEquals.
    def exitAttValuePairNotEquals(self, ctx:CorpusQLParser.AttValuePairNotEqualsContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#attValuePairDefaultEquals.
    def enterAttValuePairDefaultEquals(self, ctx:CorpusQLParser.AttValuePairDefaultEqualsContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#attValuePairDefaultEquals.
    def exitAttValuePairDefaultEquals(self, ctx:CorpusQLParser.AttValuePairDefaultEqualsContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#propName.
    def enterPropName(self, ctx:CorpusQLParser.PropNameContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#propName.
    def exitPropName(self, ctx:CorpusQLParser.PropNameContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#repetitionZeroOrMore.
    def enterRepetitionZeroOrMore(self, ctx:CorpusQLParser.RepetitionZeroOrMoreContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#repetitionZeroOrMore.
    def exitRepetitionZeroOrMore(self, ctx:CorpusQLParser.RepetitionZeroOrMoreContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#repetitionOneOrMore.
    def enterRepetitionOneOrMore(self, ctx:CorpusQLParser.RepetitionOneOrMoreContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#repetitionOneOrMore.
    def exitRepetitionOneOrMore(self, ctx:CorpusQLParser.RepetitionOneOrMoreContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#repetitionZeroOrOne.
    def enterRepetitionZeroOrOne(self, ctx:CorpusQLParser.RepetitionZeroOrOneContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#repetitionZeroOrOne.
    def exitRepetitionZeroOrOne(self, ctx:CorpusQLParser.RepetitionZeroOrOneContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#repetitionExactly.
    def enterRepetitionExactly(self, ctx:CorpusQLParser.RepetitionExactlyContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#repetitionExactly.
    def exitRepetitionExactly(self, ctx:CorpusQLParser.RepetitionExactlyContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#repetitionMinMax.
    def enterRepetitionMinMax(self, ctx:CorpusQLParser.RepetitionMinMaxContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#repetitionMinMax.
    def exitRepetitionMinMax(self, ctx:CorpusQLParser.RepetitionMinMaxContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#quotedString.
    def enterQuotedString(self, ctx:CorpusQLParser.QuotedStringContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#quotedString.
    def exitQuotedString(self, ctx:CorpusQLParser.QuotedStringContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#and.
    def enterAnd(self, ctx:CorpusQLParser.AndContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#and.
    def exitAnd(self, ctx:CorpusQLParser.AndContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#or.
    def enterOr(self, ctx:CorpusQLParser.OrContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#or.
    def exitOr(self, ctx:CorpusQLParser.OrContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#implication.
    def enterImplication(self, ctx:CorpusQLParser.ImplicationContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#implication.
    def exitImplication(self, ctx:CorpusQLParser.ImplicationContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#valuePartString.
    def enterValuePartString(self, ctx:CorpusQLParser.ValuePartStringContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#valuePartString.
    def exitValuePartString(self, ctx:CorpusQLParser.ValuePartStringContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#valuePartParenthesised.
    def enterValuePartParenthesised(self, ctx:CorpusQLParser.ValuePartParenthesisedContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#valuePartParenthesised.
    def exitValuePartParenthesised(self, ctx:CorpusQLParser.ValuePartParenthesisedContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#valueWith.
    def enterValueWith(self, ctx:CorpusQLParser.ValueWithContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#valueWith.
    def exitValueWith(self, ctx:CorpusQLParser.ValueWithContext):
        pass


    # Enter a parse tree produced by CorpusQLParser#valueWithout.
    def enterValueWithout(self, ctx:CorpusQLParser.ValueWithoutContext):
        pass

    # Exit a parse tree produced by CorpusQLParser#valueWithout.
    def exitValueWithout(self, ctx:CorpusQLParser.ValueWithoutContext):
        pass



del CorpusQLParser