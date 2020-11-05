# Generated from /Users/seantyh/langon/Sketchon/dep/../src/sketchon/cql_parser/cqlParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cqlParser import cqlParser
else:
    from cqlParser import cqlParser

# This class defines a complete generic visitor for a parse tree produced by cqlParser.

class cqlParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by cqlParser#root.
    def visitRoot(self, ctx:cqlParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cqlParser#regExp.
    def visitRegExp(self, ctx:cqlParser.RegExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cqlParser#branch.
    def visitBranch(self, ctx:cqlParser.BranchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cqlParser#piece.
    def visitPiece(self, ctx:cqlParser.PieceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cqlParser#quantifier.
    def visitQuantifier(self, ctx:cqlParser.QuantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cqlParser#quantity.
    def visitQuantity(self, ctx:cqlParser.QuantityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cqlParser#quantRange.
    def visitQuantRange(self, ctx:cqlParser.QuantRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cqlParser#quantMin.
    def visitQuantMin(self, ctx:cqlParser.QuantMinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cqlParser#atom.
    def visitAtom(self, ctx:cqlParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cqlParser#charClass.
    def visitCharClass(self, ctx:cqlParser.CharClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cqlParser#charClassExpr.
    def visitCharClassExpr(self, ctx:cqlParser.CharClassExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cqlParser#charGroup.
    def visitCharGroup(self, ctx:cqlParser.CharGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cqlParser#posCharGroup.
    def visitPosCharGroup(self, ctx:cqlParser.PosCharGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cqlParser#charRange.
    def visitCharRange(self, ctx:cqlParser.CharRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cqlParser#seRange.
    def visitSeRange(self, ctx:cqlParser.SeRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cqlParser#charOrEsc.
    def visitCharOrEsc(self, ctx:cqlParser.CharOrEscContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cqlParser#charClassEsc.
    def visitCharClassEsc(self, ctx:cqlParser.CharClassEscContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cqlParser#catEsc.
    def visitCatEsc(self, ctx:cqlParser.CatEscContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cqlParser#complEsc.
    def visitComplEsc(self, ctx:cqlParser.ComplEscContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cqlParser#charProp.
    def visitCharProp(self, ctx:cqlParser.CharPropContext):
        return self.visitChildren(ctx)



del cqlParser