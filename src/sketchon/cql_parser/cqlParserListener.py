# Generated from /Users/seantyh/langon/Sketchon/dep/../src/sketchon/cql_parser/cqlParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cqlParser import cqlParser
else:
    from cqlParser import cqlParser

# This class defines a complete listener for a parse tree produced by cqlParser.
class cqlParserListener(ParseTreeListener):

    # Enter a parse tree produced by cqlParser#root.
    def enterRoot(self, ctx:cqlParser.RootContext):
        pass

    # Exit a parse tree produced by cqlParser#root.
    def exitRoot(self, ctx:cqlParser.RootContext):
        pass


    # Enter a parse tree produced by cqlParser#regExp.
    def enterRegExp(self, ctx:cqlParser.RegExpContext):
        pass

    # Exit a parse tree produced by cqlParser#regExp.
    def exitRegExp(self, ctx:cqlParser.RegExpContext):
        pass


    # Enter a parse tree produced by cqlParser#branch.
    def enterBranch(self, ctx:cqlParser.BranchContext):
        pass

    # Exit a parse tree produced by cqlParser#branch.
    def exitBranch(self, ctx:cqlParser.BranchContext):
        pass


    # Enter a parse tree produced by cqlParser#piece.
    def enterPiece(self, ctx:cqlParser.PieceContext):
        pass

    # Exit a parse tree produced by cqlParser#piece.
    def exitPiece(self, ctx:cqlParser.PieceContext):
        pass


    # Enter a parse tree produced by cqlParser#quantifier.
    def enterQuantifier(self, ctx:cqlParser.QuantifierContext):
        pass

    # Exit a parse tree produced by cqlParser#quantifier.
    def exitQuantifier(self, ctx:cqlParser.QuantifierContext):
        pass


    # Enter a parse tree produced by cqlParser#quantity.
    def enterQuantity(self, ctx:cqlParser.QuantityContext):
        pass

    # Exit a parse tree produced by cqlParser#quantity.
    def exitQuantity(self, ctx:cqlParser.QuantityContext):
        pass


    # Enter a parse tree produced by cqlParser#quantRange.
    def enterQuantRange(self, ctx:cqlParser.QuantRangeContext):
        pass

    # Exit a parse tree produced by cqlParser#quantRange.
    def exitQuantRange(self, ctx:cqlParser.QuantRangeContext):
        pass


    # Enter a parse tree produced by cqlParser#quantMin.
    def enterQuantMin(self, ctx:cqlParser.QuantMinContext):
        pass

    # Exit a parse tree produced by cqlParser#quantMin.
    def exitQuantMin(self, ctx:cqlParser.QuantMinContext):
        pass


    # Enter a parse tree produced by cqlParser#atom.
    def enterAtom(self, ctx:cqlParser.AtomContext):
        pass

    # Exit a parse tree produced by cqlParser#atom.
    def exitAtom(self, ctx:cqlParser.AtomContext):
        pass


    # Enter a parse tree produced by cqlParser#charClass.
    def enterCharClass(self, ctx:cqlParser.CharClassContext):
        pass

    # Exit a parse tree produced by cqlParser#charClass.
    def exitCharClass(self, ctx:cqlParser.CharClassContext):
        pass


    # Enter a parse tree produced by cqlParser#charClassExpr.
    def enterCharClassExpr(self, ctx:cqlParser.CharClassExprContext):
        pass

    # Exit a parse tree produced by cqlParser#charClassExpr.
    def exitCharClassExpr(self, ctx:cqlParser.CharClassExprContext):
        pass


    # Enter a parse tree produced by cqlParser#charGroup.
    def enterCharGroup(self, ctx:cqlParser.CharGroupContext):
        pass

    # Exit a parse tree produced by cqlParser#charGroup.
    def exitCharGroup(self, ctx:cqlParser.CharGroupContext):
        pass


    # Enter a parse tree produced by cqlParser#posCharGroup.
    def enterPosCharGroup(self, ctx:cqlParser.PosCharGroupContext):
        pass

    # Exit a parse tree produced by cqlParser#posCharGroup.
    def exitPosCharGroup(self, ctx:cqlParser.PosCharGroupContext):
        pass


    # Enter a parse tree produced by cqlParser#charRange.
    def enterCharRange(self, ctx:cqlParser.CharRangeContext):
        pass

    # Exit a parse tree produced by cqlParser#charRange.
    def exitCharRange(self, ctx:cqlParser.CharRangeContext):
        pass


    # Enter a parse tree produced by cqlParser#seRange.
    def enterSeRange(self, ctx:cqlParser.SeRangeContext):
        pass

    # Exit a parse tree produced by cqlParser#seRange.
    def exitSeRange(self, ctx:cqlParser.SeRangeContext):
        pass


    # Enter a parse tree produced by cqlParser#charOrEsc.
    def enterCharOrEsc(self, ctx:cqlParser.CharOrEscContext):
        pass

    # Exit a parse tree produced by cqlParser#charOrEsc.
    def exitCharOrEsc(self, ctx:cqlParser.CharOrEscContext):
        pass


    # Enter a parse tree produced by cqlParser#charClassEsc.
    def enterCharClassEsc(self, ctx:cqlParser.CharClassEscContext):
        pass

    # Exit a parse tree produced by cqlParser#charClassEsc.
    def exitCharClassEsc(self, ctx:cqlParser.CharClassEscContext):
        pass


    # Enter a parse tree produced by cqlParser#catEsc.
    def enterCatEsc(self, ctx:cqlParser.CatEscContext):
        pass

    # Exit a parse tree produced by cqlParser#catEsc.
    def exitCatEsc(self, ctx:cqlParser.CatEscContext):
        pass


    # Enter a parse tree produced by cqlParser#complEsc.
    def enterComplEsc(self, ctx:cqlParser.ComplEscContext):
        pass

    # Exit a parse tree produced by cqlParser#complEsc.
    def exitComplEsc(self, ctx:cqlParser.ComplEscContext):
        pass


    # Enter a parse tree produced by cqlParser#charProp.
    def enterCharProp(self, ctx:cqlParser.CharPropContext):
        pass

    # Exit a parse tree produced by cqlParser#charProp.
    def exitCharProp(self, ctx:cqlParser.CharPropContext):
        pass



del cqlParser