# Generated from /Users/seantyh/langon/Sketchon/dep/../src/sketchon/cql_parser/cqlParser.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\'")
        buf.write("\u009c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\3\2\3\3\3\3\3\3\7\3\61\n")
        buf.write("\3\f\3\16\3\64\13\3\3\4\7\4\67\n\4\f\4\16\4:\13\4\3\5")
        buf.write("\3\5\5\5>\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6G\n\6\3\7")
        buf.write("\3\7\3\7\5\7L\n\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\5\n[\n\n\3\13\3\13\3\13\5\13`\n\13\3")
        buf.write("\f\3\f\3\f\3\f\3\r\5\rg\n\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\5\rr\n\r\3\r\5\ru\n\r\3\16\5\16x\n\16\3\16")
        buf.write("\3\16\6\16|\n\16\r\16\16\16}\3\17\3\17\5\17\u0082\n\17")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\5\22\u0090\n\22\3\23\3\23\3\23\3\23\3\24\3\24\3")
        buf.write("\24\3\24\3\25\3\25\3\25\2\2\26\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(\2\7\4\2\20\21#$\4\2\f\f\'\'\4\2")
        buf.write("\16\16!!\4\2\17\17\"\"\4\2\26\26\36\36\2\u00a1\2*\3\2")
        buf.write("\2\2\4-\3\2\2\2\68\3\2\2\2\b;\3\2\2\2\nF\3\2\2\2\fK\3")
        buf.write("\2\2\2\16M\3\2\2\2\20Q\3\2\2\2\22Z\3\2\2\2\24_\3\2\2\2")
        buf.write("\26a\3\2\2\2\30t\3\2\2\2\32w\3\2\2\2\34\u0081\3\2\2\2")
        buf.write("\36\u0083\3\2\2\2 \u0087\3\2\2\2\"\u008f\3\2\2\2$\u0091")
        buf.write("\3\2\2\2&\u0095\3\2\2\2(\u0099\3\2\2\2*+\5\4\3\2+,\7\2")
        buf.write("\2\3,\3\3\2\2\2-\62\5\6\4\2./\7\5\2\2/\61\5\6\4\2\60.")
        buf.write("\3\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63")
        buf.write("\5\3\2\2\2\64\62\3\2\2\2\65\67\5\b\5\2\66\65\3\2\2\2\67")
        buf.write(":\3\2\2\28\66\3\2\2\289\3\2\2\29\7\3\2\2\2:8\3\2\2\2;")
        buf.write("=\5\22\n\2<>\5\n\6\2=<\3\2\2\2=>\3\2\2\2>\t\3\2\2\2?G")
        buf.write("\7\7\2\2@G\7\b\2\2AG\7\6\2\2BC\7\13\2\2CD\5\f\7\2DE\7")
        buf.write("\22\2\2EG\3\2\2\2F?\3\2\2\2F@\3\2\2\2FA\3\2\2\2FB\3\2")
        buf.write("\2\2G\13\3\2\2\2HL\5\16\b\2IL\5\20\t\2JL\7\23\2\2KH\3")
        buf.write("\2\2\2KI\3\2\2\2KJ\3\2\2\2L\r\3\2\2\2MN\7\23\2\2NO\7\24")
        buf.write("\2\2OP\7\23\2\2P\17\3\2\2\2QR\7\23\2\2RS\7\24\2\2S\21")
        buf.write("\3\2\2\2T[\7\n\2\2U[\5\24\13\2VW\7\3\2\2WX\5\4\3\2XY\7")
        buf.write("\4\2\2Y[\3\2\2\2ZT\3\2\2\2ZU\3\2\2\2ZV\3\2\2\2[\23\3\2")
        buf.write("\2\2\\`\5\"\22\2]`\5\26\f\2^`\7\t\2\2_\\\3\2\2\2_]\3\2")
        buf.write("\2\2_^\3\2\2\2`\25\3\2\2\2ab\t\2\2\2bc\5\30\r\2cd\7%\2")
        buf.write("\2d\27\3\2\2\2eg\5\32\16\2fe\3\2\2\2fg\3\2\2\2gh\3\2\2")
        buf.write("\2hi\7&\2\2ij\7&\2\2ju\5\26\f\2kl\5\32\16\2lm\7&\2\2m")
        buf.write("n\5\26\f\2nu\3\2\2\2oq\5\32\16\2pr\7&\2\2qp\3\2\2\2qr")
        buf.write("\3\2\2\2ru\3\2\2\2su\7&\2\2tf\3\2\2\2tk\3\2\2\2to\3\2")
        buf.write("\2\2ts\3\2\2\2u\31\3\2\2\2vx\7&\2\2wv\3\2\2\2wx\3\2\2")
        buf.write("\2x{\3\2\2\2y|\5\34\17\2z|\5\"\22\2{y\3\2\2\2{z\3\2\2")
        buf.write("\2|}\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\33\3\2\2\2\177\u0082")
        buf.write("\5\36\20\2\u0080\u0082\7\'\2\2\u0081\177\3\2\2\2\u0081")
        buf.write("\u0080\3\2\2\2\u0082\35\3\2\2\2\u0083\u0084\5 \21\2\u0084")
        buf.write("\u0085\7&\2\2\u0085\u0086\5 \21\2\u0086\37\3\2\2\2\u0087")
        buf.write("\u0088\t\3\2\2\u0088!\3\2\2\2\u0089\u0090\7\f\2\2\u008a")
        buf.write("\u0090\7\37\2\2\u008b\u0090\7\r\2\2\u008c\u0090\7 \2\2")
        buf.write("\u008d\u0090\5$\23\2\u008e\u0090\5&\24\2\u008f\u0089\3")
        buf.write("\2\2\2\u008f\u008a\3\2\2\2\u008f\u008b\3\2\2\2\u008f\u008c")
        buf.write("\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u008e\3\2\2\2\u0090")
        buf.write("#\3\2\2\2\u0091\u0092\t\4\2\2\u0092\u0093\5(\25\2\u0093")
        buf.write("\u0094\7\25\2\2\u0094%\3\2\2\2\u0095\u0096\t\5\2\2\u0096")
        buf.write("\u0097\5(\25\2\u0097\u0098\7\25\2\2\u0098\'\3\2\2\2\u0099")
        buf.write("\u009a\t\6\2\2\u009a)\3\2\2\2\21\628=FKZ_fqtw{}\u0081")
        buf.write("\u008f")
        return buf.getvalue()


class cqlParser ( Parser ):

    grammarFileName = "cqlParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'|'", "'+'", "'?'", "'*'", 
                     "'.'", "<INVALID>", "'{'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "','", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "']'", "'-'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "PIPE", "PLUS", "QUESTION", 
                      "STAR", "WildcardEsc", "Char", "StartQuantity", "SingleCharEsc", 
                      "MultiCharEsc", "CatEsc", "ComplEsc", "NegCharGroup", 
                      "PosCharGroup", "EndQuantity", "QuantExact", "COMMA", 
                      "EndCategory", "IsCategory", "Letters", "Marks", "Numbers", 
                      "Punctuation", "Separators", "Symbols", "Others", 
                      "IsBlock", "NestedSingleCharEsc", "NestedMultiCharEsc", 
                      "NestedCatEsc", "NestedComplEsc", "NestedNegCharGroup", 
                      "NestedPosCharGroup", "EndCharGroup", "DASH", "XmlChar" ]

    RULE_root = 0
    RULE_regExp = 1
    RULE_branch = 2
    RULE_piece = 3
    RULE_quantifier = 4
    RULE_quantity = 5
    RULE_quantRange = 6
    RULE_quantMin = 7
    RULE_atom = 8
    RULE_charClass = 9
    RULE_charClassExpr = 10
    RULE_charGroup = 11
    RULE_posCharGroup = 12
    RULE_charRange = 13
    RULE_seRange = 14
    RULE_charOrEsc = 15
    RULE_charClassEsc = 16
    RULE_catEsc = 17
    RULE_complEsc = 18
    RULE_charProp = 19

    ruleNames =  [ "root", "regExp", "branch", "piece", "quantifier", "quantity", 
                   "quantRange", "quantMin", "atom", "charClass", "charClassExpr", 
                   "charGroup", "posCharGroup", "charRange", "seRange", 
                   "charOrEsc", "charClassEsc", "catEsc", "complEsc", "charProp" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    PIPE=3
    PLUS=4
    QUESTION=5
    STAR=6
    WildcardEsc=7
    Char=8
    StartQuantity=9
    SingleCharEsc=10
    MultiCharEsc=11
    CatEsc=12
    ComplEsc=13
    NegCharGroup=14
    PosCharGroup=15
    EndQuantity=16
    QuantExact=17
    COMMA=18
    EndCategory=19
    IsCategory=20
    Letters=21
    Marks=22
    Numbers=23
    Punctuation=24
    Separators=25
    Symbols=26
    Others=27
    IsBlock=28
    NestedSingleCharEsc=29
    NestedMultiCharEsc=30
    NestedCatEsc=31
    NestedComplEsc=32
    NestedNegCharGroup=33
    NestedPosCharGroup=34
    EndCharGroup=35
    DASH=36
    XmlChar=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def regExp(self):
            return self.getTypedRuleContext(cqlParser.RegExpContext,0)


        def EOF(self):
            return self.getToken(cqlParser.EOF, 0)

        def getRuleIndex(self):
            return cqlParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = cqlParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.regExp()
            self.state = 41
            self.match(cqlParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def branch(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cqlParser.BranchContext)
            else:
                return self.getTypedRuleContext(cqlParser.BranchContext,i)


        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(cqlParser.PIPE)
            else:
                return self.getToken(cqlParser.PIPE, i)

        def getRuleIndex(self):
            return cqlParser.RULE_regExp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegExp" ):
                listener.enterRegExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegExp" ):
                listener.exitRegExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegExp" ):
                return visitor.visitRegExp(self)
            else:
                return visitor.visitChildren(self)




    def regExp(self):

        localctx = cqlParser.RegExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_regExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.branch()
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cqlParser.PIPE:
                self.state = 44
                self.match(cqlParser.PIPE)
                self.state = 45
                self.branch()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BranchContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def piece(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cqlParser.PieceContext)
            else:
                return self.getTypedRuleContext(cqlParser.PieceContext,i)


        def getRuleIndex(self):
            return cqlParser.RULE_branch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBranch" ):
                listener.enterBranch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBranch" ):
                listener.exitBranch(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBranch" ):
                return visitor.visitBranch(self)
            else:
                return visitor.visitChildren(self)




    def branch(self):

        localctx = cqlParser.BranchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_branch)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cqlParser.LPAREN) | (1 << cqlParser.WildcardEsc) | (1 << cqlParser.Char) | (1 << cqlParser.SingleCharEsc) | (1 << cqlParser.MultiCharEsc) | (1 << cqlParser.CatEsc) | (1 << cqlParser.ComplEsc) | (1 << cqlParser.NegCharGroup) | (1 << cqlParser.PosCharGroup) | (1 << cqlParser.NestedSingleCharEsc) | (1 << cqlParser.NestedMultiCharEsc) | (1 << cqlParser.NestedCatEsc) | (1 << cqlParser.NestedComplEsc) | (1 << cqlParser.NestedNegCharGroup) | (1 << cqlParser.NestedPosCharGroup))) != 0):
                self.state = 51
                self.piece()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PieceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(cqlParser.AtomContext,0)


        def quantifier(self):
            return self.getTypedRuleContext(cqlParser.QuantifierContext,0)


        def getRuleIndex(self):
            return cqlParser.RULE_piece

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPiece" ):
                listener.enterPiece(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPiece" ):
                listener.exitPiece(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPiece" ):
                return visitor.visitPiece(self)
            else:
                return visitor.visitChildren(self)




    def piece(self):

        localctx = cqlParser.PieceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_piece)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.atom()
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cqlParser.PLUS) | (1 << cqlParser.QUESTION) | (1 << cqlParser.STAR) | (1 << cqlParser.StartQuantity))) != 0):
                self.state = 58
                self.quantifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUESTION(self):
            return self.getToken(cqlParser.QUESTION, 0)

        def STAR(self):
            return self.getToken(cqlParser.STAR, 0)

        def PLUS(self):
            return self.getToken(cqlParser.PLUS, 0)

        def StartQuantity(self):
            return self.getToken(cqlParser.StartQuantity, 0)

        def quantity(self):
            return self.getTypedRuleContext(cqlParser.QuantityContext,0)


        def EndQuantity(self):
            return self.getToken(cqlParser.EndQuantity, 0)

        def getRuleIndex(self):
            return cqlParser.RULE_quantifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantifier" ):
                listener.enterQuantifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantifier" ):
                listener.exitQuantifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantifier" ):
                return visitor.visitQuantifier(self)
            else:
                return visitor.visitChildren(self)




    def quantifier(self):

        localctx = cqlParser.QuantifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_quantifier)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [cqlParser.QUESTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(cqlParser.QUESTION)
                pass
            elif token in [cqlParser.STAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(cqlParser.STAR)
                pass
            elif token in [cqlParser.PLUS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.match(cqlParser.PLUS)
                pass
            elif token in [cqlParser.StartQuantity]:
                self.enterOuterAlt(localctx, 4)
                self.state = 64
                self.match(cqlParser.StartQuantity)
                self.state = 65
                self.quantity()
                self.state = 66
                self.match(cqlParser.EndQuantity)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantityContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quantRange(self):
            return self.getTypedRuleContext(cqlParser.QuantRangeContext,0)


        def quantMin(self):
            return self.getTypedRuleContext(cqlParser.QuantMinContext,0)


        def QuantExact(self):
            return self.getToken(cqlParser.QuantExact, 0)

        def getRuleIndex(self):
            return cqlParser.RULE_quantity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantity" ):
                listener.enterQuantity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantity" ):
                listener.exitQuantity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantity" ):
                return visitor.visitQuantity(self)
            else:
                return visitor.visitChildren(self)




    def quantity(self):

        localctx = cqlParser.QuantityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_quantity)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.quantRange()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.quantMin()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.match(cqlParser.QuantExact)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantRangeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QuantExact(self, i:int=None):
            if i is None:
                return self.getTokens(cqlParser.QuantExact)
            else:
                return self.getToken(cqlParser.QuantExact, i)

        def COMMA(self):
            return self.getToken(cqlParser.COMMA, 0)

        def getRuleIndex(self):
            return cqlParser.RULE_quantRange

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantRange" ):
                listener.enterQuantRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantRange" ):
                listener.exitQuantRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantRange" ):
                return visitor.visitQuantRange(self)
            else:
                return visitor.visitChildren(self)




    def quantRange(self):

        localctx = cqlParser.QuantRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_quantRange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(cqlParser.QuantExact)
            self.state = 76
            self.match(cqlParser.COMMA)
            self.state = 77
            self.match(cqlParser.QuantExact)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantMinContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QuantExact(self):
            return self.getToken(cqlParser.QuantExact, 0)

        def COMMA(self):
            return self.getToken(cqlParser.COMMA, 0)

        def getRuleIndex(self):
            return cqlParser.RULE_quantMin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantMin" ):
                listener.enterQuantMin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantMin" ):
                listener.exitQuantMin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantMin" ):
                return visitor.visitQuantMin(self)
            else:
                return visitor.visitChildren(self)




    def quantMin(self):

        localctx = cqlParser.QuantMinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_quantMin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(cqlParser.QuantExact)
            self.state = 80
            self.match(cqlParser.COMMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Char(self):
            return self.getToken(cqlParser.Char, 0)

        def charClass(self):
            return self.getTypedRuleContext(cqlParser.CharClassContext,0)


        def LPAREN(self):
            return self.getToken(cqlParser.LPAREN, 0)

        def regExp(self):
            return self.getTypedRuleContext(cqlParser.RegExpContext,0)


        def RPAREN(self):
            return self.getToken(cqlParser.RPAREN, 0)

        def getRuleIndex(self):
            return cqlParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = cqlParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_atom)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [cqlParser.Char]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.match(cqlParser.Char)
                pass
            elif token in [cqlParser.WildcardEsc, cqlParser.SingleCharEsc, cqlParser.MultiCharEsc, cqlParser.CatEsc, cqlParser.ComplEsc, cqlParser.NegCharGroup, cqlParser.PosCharGroup, cqlParser.NestedSingleCharEsc, cqlParser.NestedMultiCharEsc, cqlParser.NestedCatEsc, cqlParser.NestedComplEsc, cqlParser.NestedNegCharGroup, cqlParser.NestedPosCharGroup]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.charClass()
                pass
            elif token in [cqlParser.LPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.match(cqlParser.LPAREN)
                self.state = 85
                self.regExp()
                self.state = 86
                self.match(cqlParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharClassContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def charClassEsc(self):
            return self.getTypedRuleContext(cqlParser.CharClassEscContext,0)


        def charClassExpr(self):
            return self.getTypedRuleContext(cqlParser.CharClassExprContext,0)


        def WildcardEsc(self):
            return self.getToken(cqlParser.WildcardEsc, 0)

        def getRuleIndex(self):
            return cqlParser.RULE_charClass

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharClass" ):
                listener.enterCharClass(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharClass" ):
                listener.exitCharClass(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharClass" ):
                return visitor.visitCharClass(self)
            else:
                return visitor.visitChildren(self)




    def charClass(self):

        localctx = cqlParser.CharClassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_charClass)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [cqlParser.SingleCharEsc, cqlParser.MultiCharEsc, cqlParser.CatEsc, cqlParser.ComplEsc, cqlParser.NestedSingleCharEsc, cqlParser.NestedMultiCharEsc, cqlParser.NestedCatEsc, cqlParser.NestedComplEsc]:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.charClassEsc()
                pass
            elif token in [cqlParser.NegCharGroup, cqlParser.PosCharGroup, cqlParser.NestedNegCharGroup, cqlParser.NestedPosCharGroup]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.charClassExpr()
                pass
            elif token in [cqlParser.WildcardEsc]:
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                self.match(cqlParser.WildcardEsc)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharClassExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def charGroup(self):
            return self.getTypedRuleContext(cqlParser.CharGroupContext,0)


        def EndCharGroup(self):
            return self.getToken(cqlParser.EndCharGroup, 0)

        def NegCharGroup(self):
            return self.getToken(cqlParser.NegCharGroup, 0)

        def NestedNegCharGroup(self):
            return self.getToken(cqlParser.NestedNegCharGroup, 0)

        def PosCharGroup(self):
            return self.getToken(cqlParser.PosCharGroup, 0)

        def NestedPosCharGroup(self):
            return self.getToken(cqlParser.NestedPosCharGroup, 0)

        def getRuleIndex(self):
            return cqlParser.RULE_charClassExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharClassExpr" ):
                listener.enterCharClassExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharClassExpr" ):
                listener.exitCharClassExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharClassExpr" ):
                return visitor.visitCharClassExpr(self)
            else:
                return visitor.visitChildren(self)




    def charClassExpr(self):

        localctx = cqlParser.CharClassExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_charClassExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cqlParser.NegCharGroup) | (1 << cqlParser.PosCharGroup) | (1 << cqlParser.NestedNegCharGroup) | (1 << cqlParser.NestedPosCharGroup))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 96
            self.charGroup()
            self.state = 97
            self.match(cqlParser.EndCharGroup)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharGroupContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DASH(self, i:int=None):
            if i is None:
                return self.getTokens(cqlParser.DASH)
            else:
                return self.getToken(cqlParser.DASH, i)

        def charClassExpr(self):
            return self.getTypedRuleContext(cqlParser.CharClassExprContext,0)


        def posCharGroup(self):
            return self.getTypedRuleContext(cqlParser.PosCharGroupContext,0)


        def getRuleIndex(self):
            return cqlParser.RULE_charGroup

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharGroup" ):
                listener.enterCharGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharGroup" ):
                listener.exitCharGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharGroup" ):
                return visitor.visitCharGroup(self)
            else:
                return visitor.visitChildren(self)




    def charGroup(self):

        localctx = cqlParser.CharGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_charGroup)
        self._la = 0 # Token type
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 99
                    self.posCharGroup()


                self.state = 102
                self.match(cqlParser.DASH)
                self.state = 103
                self.match(cqlParser.DASH)
                self.state = 104
                self.charClassExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.posCharGroup()
                self.state = 106
                self.match(cqlParser.DASH)
                self.state = 107
                self.charClassExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.posCharGroup()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==cqlParser.DASH:
                    self.state = 110
                    self.match(cqlParser.DASH)


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 113
                self.match(cqlParser.DASH)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PosCharGroupContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DASH(self):
            return self.getToken(cqlParser.DASH, 0)

        def charRange(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cqlParser.CharRangeContext)
            else:
                return self.getTypedRuleContext(cqlParser.CharRangeContext,i)


        def charClassEsc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cqlParser.CharClassEscContext)
            else:
                return self.getTypedRuleContext(cqlParser.CharClassEscContext,i)


        def getRuleIndex(self):
            return cqlParser.RULE_posCharGroup

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPosCharGroup" ):
                listener.enterPosCharGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPosCharGroup" ):
                listener.exitPosCharGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPosCharGroup" ):
                return visitor.visitPosCharGroup(self)
            else:
                return visitor.visitChildren(self)




    def posCharGroup(self):

        localctx = cqlParser.PosCharGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_posCharGroup)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cqlParser.DASH:
                self.state = 116
                self.match(cqlParser.DASH)


            self.state = 121 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 121
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 119
                    self.charRange()
                    pass

                elif la_ == 2:
                    self.state = 120
                    self.charClassEsc()
                    pass


                self.state = 123 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cqlParser.SingleCharEsc) | (1 << cqlParser.MultiCharEsc) | (1 << cqlParser.CatEsc) | (1 << cqlParser.ComplEsc) | (1 << cqlParser.NestedSingleCharEsc) | (1 << cqlParser.NestedMultiCharEsc) | (1 << cqlParser.NestedCatEsc) | (1 << cqlParser.NestedComplEsc) | (1 << cqlParser.XmlChar))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharRangeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def seRange(self):
            return self.getTypedRuleContext(cqlParser.SeRangeContext,0)


        def XmlChar(self):
            return self.getToken(cqlParser.XmlChar, 0)

        def getRuleIndex(self):
            return cqlParser.RULE_charRange

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharRange" ):
                listener.enterCharRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharRange" ):
                listener.exitCharRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharRange" ):
                return visitor.visitCharRange(self)
            else:
                return visitor.visitChildren(self)




    def charRange(self):

        localctx = cqlParser.CharRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_charRange)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.seRange()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.match(cqlParser.XmlChar)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeRangeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def charOrEsc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cqlParser.CharOrEscContext)
            else:
                return self.getTypedRuleContext(cqlParser.CharOrEscContext,i)


        def DASH(self):
            return self.getToken(cqlParser.DASH, 0)

        def getRuleIndex(self):
            return cqlParser.RULE_seRange

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeRange" ):
                listener.enterSeRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeRange" ):
                listener.exitSeRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeRange" ):
                return visitor.visitSeRange(self)
            else:
                return visitor.visitChildren(self)




    def seRange(self):

        localctx = cqlParser.SeRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_seRange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.charOrEsc()
            self.state = 130
            self.match(cqlParser.DASH)
            self.state = 131
            self.charOrEsc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharOrEscContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def XmlChar(self):
            return self.getToken(cqlParser.XmlChar, 0)

        def SingleCharEsc(self):
            return self.getToken(cqlParser.SingleCharEsc, 0)

        def getRuleIndex(self):
            return cqlParser.RULE_charOrEsc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharOrEsc" ):
                listener.enterCharOrEsc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharOrEsc" ):
                listener.exitCharOrEsc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharOrEsc" ):
                return visitor.visitCharOrEsc(self)
            else:
                return visitor.visitChildren(self)




    def charOrEsc(self):

        localctx = cqlParser.CharOrEscContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_charOrEsc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            _la = self._input.LA(1)
            if not(_la==cqlParser.SingleCharEsc or _la==cqlParser.XmlChar):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharClassEscContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SingleCharEsc(self):
            return self.getToken(cqlParser.SingleCharEsc, 0)

        def NestedSingleCharEsc(self):
            return self.getToken(cqlParser.NestedSingleCharEsc, 0)

        def MultiCharEsc(self):
            return self.getToken(cqlParser.MultiCharEsc, 0)

        def NestedMultiCharEsc(self):
            return self.getToken(cqlParser.NestedMultiCharEsc, 0)

        def catEsc(self):
            return self.getTypedRuleContext(cqlParser.CatEscContext,0)


        def complEsc(self):
            return self.getTypedRuleContext(cqlParser.ComplEscContext,0)


        def getRuleIndex(self):
            return cqlParser.RULE_charClassEsc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharClassEsc" ):
                listener.enterCharClassEsc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharClassEsc" ):
                listener.exitCharClassEsc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharClassEsc" ):
                return visitor.visitCharClassEsc(self)
            else:
                return visitor.visitChildren(self)




    def charClassEsc(self):

        localctx = cqlParser.CharClassEscContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_charClassEsc)
        try:
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [cqlParser.SingleCharEsc]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(cqlParser.SingleCharEsc)
                pass
            elif token in [cqlParser.NestedSingleCharEsc]:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.match(cqlParser.NestedSingleCharEsc)
                pass
            elif token in [cqlParser.MultiCharEsc]:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                self.match(cqlParser.MultiCharEsc)
                pass
            elif token in [cqlParser.NestedMultiCharEsc]:
                self.enterOuterAlt(localctx, 4)
                self.state = 138
                self.match(cqlParser.NestedMultiCharEsc)
                pass
            elif token in [cqlParser.CatEsc, cqlParser.NestedCatEsc]:
                self.enterOuterAlt(localctx, 5)
                self.state = 139
                self.catEsc()
                pass
            elif token in [cqlParser.ComplEsc, cqlParser.NestedComplEsc]:
                self.enterOuterAlt(localctx, 6)
                self.state = 140
                self.complEsc()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CatEscContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def charProp(self):
            return self.getTypedRuleContext(cqlParser.CharPropContext,0)


        def EndCategory(self):
            return self.getToken(cqlParser.EndCategory, 0)

        def CatEsc(self):
            return self.getToken(cqlParser.CatEsc, 0)

        def NestedCatEsc(self):
            return self.getToken(cqlParser.NestedCatEsc, 0)

        def getRuleIndex(self):
            return cqlParser.RULE_catEsc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatEsc" ):
                listener.enterCatEsc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatEsc" ):
                listener.exitCatEsc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCatEsc" ):
                return visitor.visitCatEsc(self)
            else:
                return visitor.visitChildren(self)




    def catEsc(self):

        localctx = cqlParser.CatEscContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_catEsc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            _la = self._input.LA(1)
            if not(_la==cqlParser.CatEsc or _la==cqlParser.NestedCatEsc):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 144
            self.charProp()
            self.state = 145
            self.match(cqlParser.EndCategory)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComplEscContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def charProp(self):
            return self.getTypedRuleContext(cqlParser.CharPropContext,0)


        def EndCategory(self):
            return self.getToken(cqlParser.EndCategory, 0)

        def ComplEsc(self):
            return self.getToken(cqlParser.ComplEsc, 0)

        def NestedComplEsc(self):
            return self.getToken(cqlParser.NestedComplEsc, 0)

        def getRuleIndex(self):
            return cqlParser.RULE_complEsc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplEsc" ):
                listener.enterComplEsc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplEsc" ):
                listener.exitComplEsc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplEsc" ):
                return visitor.visitComplEsc(self)
            else:
                return visitor.visitChildren(self)




    def complEsc(self):

        localctx = cqlParser.ComplEscContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_complEsc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            _la = self._input.LA(1)
            if not(_la==cqlParser.ComplEsc or _la==cqlParser.NestedComplEsc):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 148
            self.charProp()
            self.state = 149
            self.match(cqlParser.EndCategory)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharPropContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IsCategory(self):
            return self.getToken(cqlParser.IsCategory, 0)

        def IsBlock(self):
            return self.getToken(cqlParser.IsBlock, 0)

        def getRuleIndex(self):
            return cqlParser.RULE_charProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharProp" ):
                listener.enterCharProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharProp" ):
                listener.exitCharProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharProp" ):
                return visitor.visitCharProp(self)
            else:
                return visitor.visitChildren(self)




    def charProp(self):

        localctx = cqlParser.CharPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_charProp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            _la = self._input.LA(1)
            if not(_la==cqlParser.IsCategory or _la==cqlParser.IsBlock):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





