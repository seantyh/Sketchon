# Generated from /Users/seantyh/langon/Sketchon/dep/../src/sketchon/cql_parser/CorpusQL.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\36")
        buf.write("\u00b0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\3\3\3\3\3\3\3\5\3/\n\3\3\4\3\4\5")
        buf.write("\4\63\n\4\3\5\3\5\3\5\3\5\5\59\n\5\3\6\6\6<\n\6\r\6\16")
        buf.write("\6=\3\7\3\7\5\7B\n\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7J\n\7")
        buf.write("\3\7\5\7M\n\7\3\b\3\b\5\bQ\n\b\3\b\3\b\7\bU\n\b\f\b\16")
        buf.write("\bX\13\b\3\b\5\b[\n\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\5\nf\n\n\3\n\5\ni\n\n\3\13\3\13\3\f\3\f\3\f\3\f\5")
        buf.write("\fq\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\rz\n\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u0085\n\16\3")
        buf.write("\17\3\17\3\17\5\17\u008a\n\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\5\20\u0096\n\20\3\20\5\20\u0099")
        buf.write("\n\20\3\21\3\21\3\22\3\22\3\22\5\22\u00a0\n\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\5\23\u00a7\n\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\5\24\u00ae\n\24\3\24\2\2\25\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&\2\4\3\2\t\n\3\2\13\f\2\u00b8\2")
        buf.write("(\3\2\2\2\4*\3\2\2\2\6\62\3\2\2\2\b\64\3\2\2\2\n;\3\2")
        buf.write("\2\2\fA\3\2\2\2\16N\3\2\2\2\20^\3\2\2\2\22h\3\2\2\2\24")
        buf.write("j\3\2\2\2\26l\3\2\2\2\30y\3\2\2\2\32\u0084\3\2\2\2\34")
        buf.write("\u0086\3\2\2\2\36\u0098\3\2\2\2 \u009a\3\2\2\2\"\u009f")
        buf.write("\3\2\2\2$\u00a6\3\2\2\2&\u00ad\3\2\2\2()\5\4\3\2)\3\3")
        buf.write("\2\2\2*.\5\b\5\2+,\5\6\4\2,-\5\4\3\2-/\3\2\2\2.+\3\2\2")
        buf.write("\2./\3\2\2\2/\5\3\2\2\2\60\63\7\7\2\2\61\63\7\b\2\2\62")
        buf.write("\60\3\2\2\2\62\61\3\2\2\2\63\7\3\2\2\2\648\5\n\6\2\65")
        buf.write("\66\5\"\22\2\66\67\5\b\5\2\679\3\2\2\28\65\3\2\2\289\3")
        buf.write("\2\2\29\t\3\2\2\2:<\5\f\7\2;:\3\2\2\2<=\3\2\2\2=;\3\2")
        buf.write("\2\2=>\3\2\2\2>\13\3\2\2\2?@\t\2\2\2@B\7\3\2\2A?\3\2\2")
        buf.write("\2AB\3\2\2\2BI\3\2\2\2CJ\5\16\b\2DJ\5\22\n\2EF\7\24\2")
        buf.write("\2FG\5\4\3\2GH\7\25\2\2HJ\3\2\2\2IC\3\2\2\2ID\3\2\2\2")
        buf.write("IE\3\2\2\2JL\3\2\2\2KM\5\36\20\2LK\3\2\2\2LM\3\2\2\2M")
        buf.write("\r\3\2\2\2NP\7\16\2\2OQ\7\20\2\2PO\3\2\2\2PQ\3\2\2\2Q")
        buf.write("R\3\2\2\2RV\7\t\2\2SU\5\20\t\2TS\3\2\2\2UX\3\2\2\2VT\3")
        buf.write("\2\2\2VW\3\2\2\2WZ\3\2\2\2XV\3\2\2\2Y[\7\20\2\2ZY\3\2")
        buf.write("\2\2Z[\3\2\2\2[\\\3\2\2\2\\]\7\17\2\2]\17\3\2\2\2^_\7")
        buf.write("\t\2\2_`\7\21\2\2`a\5 \21\2a\21\3\2\2\2bi\5\24\13\2ce")
        buf.write("\7\22\2\2df\5\26\f\2ed\3\2\2\2ef\3\2\2\2fg\3\2\2\2gi\7")
        buf.write("\23\2\2hb\3\2\2\2hc\3\2\2\2i\23\3\2\2\2jk\5 \21\2k\25")
        buf.write("\3\2\2\2lp\5\30\r\2mn\5\"\22\2no\5\26\f\2oq\3\2\2\2pm")
        buf.write("\3\2\2\2pq\3\2\2\2q\27\3\2\2\2rz\5\32\16\2st\7\24\2\2")
        buf.write("tu\5\26\f\2uv\7\25\2\2vz\3\2\2\2wx\7\26\2\2xz\5\30\r\2")
        buf.write("yr\3\2\2\2ys\3\2\2\2yw\3\2\2\2z\31\3\2\2\2{|\5\34\17\2")
        buf.write("|}\7\21\2\2}~\5$\23\2~\u0085\3\2\2\2\177\u0080\5\34\17")
        buf.write("\2\u0080\u0081\7\4\2\2\u0081\u0082\5$\23\2\u0082\u0085")
        buf.write("\3\2\2\2\u0083\u0085\5$\23\2\u0084{\3\2\2\2\u0084\177")
        buf.write("\3\2\2\2\u0084\u0083\3\2\2\2\u0085\33\3\2\2\2\u0086\u0089")
        buf.write("\7\t\2\2\u0087\u0088\7\20\2\2\u0088\u008a\7\t\2\2\u0089")
        buf.write("\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a\35\3\2\2\2\u008b")
        buf.write("\u0099\7\27\2\2\u008c\u0099\7\30\2\2\u008d\u0099\7\31")
        buf.write("\2\2\u008e\u008f\7\32\2\2\u008f\u0090\7\n\2\2\u0090\u0099")
        buf.write("\7\33\2\2\u0091\u0092\7\32\2\2\u0092\u0093\7\n\2\2\u0093")
        buf.write("\u0095\7\5\2\2\u0094\u0096\7\n\2\2\u0095\u0094\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0099\7")
        buf.write("\33\2\2\u0098\u008b\3\2\2\2\u0098\u008c\3\2\2\2\u0098")
        buf.write("\u008d\3\2\2\2\u0098\u008e\3\2\2\2\u0098\u0091\3\2\2\2")
        buf.write("\u0099\37\3\2\2\2\u009a\u009b\t\3\2\2\u009b!\3\2\2\2\u009c")
        buf.write("\u00a0\7\34\2\2\u009d\u00a0\7\35\2\2\u009e\u00a0\7\6\2")
        buf.write("\2\u009f\u009c\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u009e")
        buf.write("\3\2\2\2\u00a0#\3\2\2\2\u00a1\u00a7\5 \21\2\u00a2\u00a3")
        buf.write("\7\24\2\2\u00a3\u00a4\5&\24\2\u00a4\u00a5\7\25\2\2\u00a5")
        buf.write("\u00a7\3\2\2\2\u00a6\u00a1\3\2\2\2\u00a6\u00a2\3\2\2\2")
        buf.write("\u00a7%\3\2\2\2\u00a8\u00a9\5$\23\2\u00a9\u00aa\5\"\22")
        buf.write("\2\u00aa\u00ab\5&\24\2\u00ab\u00ae\3\2\2\2\u00ac\u00ae")
        buf.write("\5$\23\2\u00ad\u00a8\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae")
        buf.write("\'\3\2\2\2\27.\628=AILPVZehpy\u0084\u0089\u0095\u0098")
        buf.write("\u009f\u00a6\u00ad")
        return buf.getvalue()


class CorpusQLParser ( Parser ):

    grammarFileName = "CorpusQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'!='", "','", "'->'", "'WITHIN'", 
                     "'CONTAINING'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'<'", "'>'", "'/'", "'='", 
                     "'['", "']'", "'('", "')'", "'!'", "'*'", "'+'", "'?'", 
                     "'{'", "'}'", "'&'", "'|'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WITHIN", "CONTAINING", "NAME", "NUMBER", 
                      "DOUBLE_QUOTED_STRING", "SINGLE_QUOTED_STRING", "WS", 
                      "LT", "GT", "SOLIDUS", "EQUALS", "LEFT_SQUARE_BRACKET", 
                      "RIGHT_SQUARE_BRACKET", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", 
                      "EXCLAMATION_MARK", "ASTERISK", "PLUS", "QUESTION_MARK", 
                      "LEFT_CURLY_BRACKET", "LEFT_RIGHT_BRACKET", "AMPERSAND", 
                      "VERTICAL_LINE", "HYPHEN_MINUS" ]

    RULE_query = 0
    RULE_complexQuery = 1
    RULE_queryOperator = 2
    RULE_simpleQuery = 3
    RULE_sequence = 4
    RULE_sequencePart = 5
    RULE_tag = 6
    RULE_attribute = 7
    RULE_position = 8
    RULE_positionWord = 9
    RULE_positionLong = 10
    RULE_positionLongPart = 11
    RULE_attValuePair = 12
    RULE_propName = 13
    RULE_repetitionAmount = 14
    RULE_quotedString = 15
    RULE_booleanOperator = 16
    RULE_valuePart = 17
    RULE_value = 18

    ruleNames =  [ "query", "complexQuery", "queryOperator", "simpleQuery", 
                   "sequence", "sequencePart", "tag", "attribute", "position", 
                   "positionWord", "positionLong", "positionLongPart", "attValuePair", 
                   "propName", "repetitionAmount", "quotedString", "booleanOperator", 
                   "valuePart", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    WITHIN=5
    CONTAINING=6
    NAME=7
    NUMBER=8
    DOUBLE_QUOTED_STRING=9
    SINGLE_QUOTED_STRING=10
    WS=11
    LT=12
    GT=13
    SOLIDUS=14
    EQUALS=15
    LEFT_SQUARE_BRACKET=16
    RIGHT_SQUARE_BRACKET=17
    LEFT_PARENTHESIS=18
    RIGHT_PARENTHESIS=19
    EXCLAMATION_MARK=20
    ASTERISK=21
    PLUS=22
    QUESTION_MARK=23
    LEFT_CURLY_BRACKET=24
    LEFT_RIGHT_BRACKET=25
    AMPERSAND=26
    VERTICAL_LINE=27
    HYPHEN_MINUS=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def complexQuery(self):
            return self.getTypedRuleContext(CorpusQLParser.ComplexQueryContext,0)


        def getRuleIndex(self):
            return CorpusQLParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = CorpusQLParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.complexQuery()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComplexQueryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleQuery(self):
            return self.getTypedRuleContext(CorpusQLParser.SimpleQueryContext,0)


        def queryOperator(self):
            return self.getTypedRuleContext(CorpusQLParser.QueryOperatorContext,0)


        def complexQuery(self):
            return self.getTypedRuleContext(CorpusQLParser.ComplexQueryContext,0)


        def getRuleIndex(self):
            return CorpusQLParser.RULE_complexQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplexQuery" ):
                listener.enterComplexQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplexQuery" ):
                listener.exitComplexQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexQuery" ):
                return visitor.visitComplexQuery(self)
            else:
                return visitor.visitChildren(self)




    def complexQuery(self):

        localctx = CorpusQLParser.ComplexQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_complexQuery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.simpleQuery()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CorpusQLParser.WITHIN or _la==CorpusQLParser.CONTAINING:
                self.state = 41
                self.queryOperator()
                self.state = 42
                self.complexQuery()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CorpusQLParser.RULE_queryOperator

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WithinContext(QueryOperatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusQLParser.QueryOperatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WITHIN(self):
            return self.getToken(CorpusQLParser.WITHIN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWithin" ):
                listener.enterWithin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWithin" ):
                listener.exitWithin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWithin" ):
                return visitor.visitWithin(self)
            else:
                return visitor.visitChildren(self)


    class ContainingContext(QueryOperatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusQLParser.QueryOperatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONTAINING(self):
            return self.getToken(CorpusQLParser.CONTAINING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContaining" ):
                listener.enterContaining(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContaining" ):
                listener.exitContaining(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContaining" ):
                return visitor.visitContaining(self)
            else:
                return visitor.visitChildren(self)



    def queryOperator(self):

        localctx = CorpusQLParser.QueryOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_queryOperator)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CorpusQLParser.WITHIN]:
                localctx = CorpusQLParser.WithinContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(CorpusQLParser.WITHIN)
                pass
            elif token in [CorpusQLParser.CONTAINING]:
                localctx = CorpusQLParser.ContainingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(CorpusQLParser.CONTAINING)
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


    class SimpleQueryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sequence(self):
            return self.getTypedRuleContext(CorpusQLParser.SequenceContext,0)


        def booleanOperator(self):
            return self.getTypedRuleContext(CorpusQLParser.BooleanOperatorContext,0)


        def simpleQuery(self):
            return self.getTypedRuleContext(CorpusQLParser.SimpleQueryContext,0)


        def getRuleIndex(self):
            return CorpusQLParser.RULE_simpleQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleQuery" ):
                listener.enterSimpleQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleQuery" ):
                listener.exitSimpleQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleQuery" ):
                return visitor.visitSimpleQuery(self)
            else:
                return visitor.visitChildren(self)




    def simpleQuery(self):

        localctx = CorpusQLParser.SimpleQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_simpleQuery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.sequence()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CorpusQLParser.T__3) | (1 << CorpusQLParser.AMPERSAND) | (1 << CorpusQLParser.VERTICAL_LINE))) != 0):
                self.state = 51
                self.booleanOperator()
                self.state = 52
                self.simpleQuery()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SequenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sequencePart(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CorpusQLParser.SequencePartContext)
            else:
                return self.getTypedRuleContext(CorpusQLParser.SequencePartContext,i)


        def getRuleIndex(self):
            return CorpusQLParser.RULE_sequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequence" ):
                listener.enterSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequence" ):
                listener.exitSequence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequence" ):
                return visitor.visitSequence(self)
            else:
                return visitor.visitChildren(self)




    def sequence(self):

        localctx = CorpusQLParser.SequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sequence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 56
                self.sequencePart()
                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CorpusQLParser.NAME) | (1 << CorpusQLParser.NUMBER) | (1 << CorpusQLParser.DOUBLE_QUOTED_STRING) | (1 << CorpusQLParser.SINGLE_QUOTED_STRING) | (1 << CorpusQLParser.LT) | (1 << CorpusQLParser.LEFT_SQUARE_BRACKET) | (1 << CorpusQLParser.LEFT_PARENTHESIS))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SequencePartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tag(self):
            return self.getTypedRuleContext(CorpusQLParser.TagContext,0)


        def position(self):
            return self.getTypedRuleContext(CorpusQLParser.PositionContext,0)


        def LEFT_PARENTHESIS(self):
            return self.getToken(CorpusQLParser.LEFT_PARENTHESIS, 0)

        def complexQuery(self):
            return self.getTypedRuleContext(CorpusQLParser.ComplexQueryContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(CorpusQLParser.RIGHT_PARENTHESIS, 0)

        def repetitionAmount(self):
            return self.getTypedRuleContext(CorpusQLParser.RepetitionAmountContext,0)


        def NAME(self):
            return self.getToken(CorpusQLParser.NAME, 0)

        def NUMBER(self):
            return self.getToken(CorpusQLParser.NUMBER, 0)

        def getRuleIndex(self):
            return CorpusQLParser.RULE_sequencePart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequencePart" ):
                listener.enterSequencePart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequencePart" ):
                listener.exitSequencePart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequencePart" ):
                return visitor.visitSequencePart(self)
            else:
                return visitor.visitChildren(self)




    def sequencePart(self):

        localctx = CorpusQLParser.SequencePartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_sequencePart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CorpusQLParser.NAME or _la==CorpusQLParser.NUMBER:
                self.state = 61
                _la = self._input.LA(1)
                if not(_la==CorpusQLParser.NAME or _la==CorpusQLParser.NUMBER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 62
                self.match(CorpusQLParser.T__0)


            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CorpusQLParser.LT]:
                self.state = 65
                self.tag()
                pass
            elif token in [CorpusQLParser.DOUBLE_QUOTED_STRING, CorpusQLParser.SINGLE_QUOTED_STRING, CorpusQLParser.LEFT_SQUARE_BRACKET]:
                self.state = 66
                self.position()
                pass
            elif token in [CorpusQLParser.LEFT_PARENTHESIS]:
                self.state = 67
                self.match(CorpusQLParser.LEFT_PARENTHESIS)
                self.state = 68
                self.complexQuery()
                self.state = 69
                self.match(CorpusQLParser.RIGHT_PARENTHESIS)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CorpusQLParser.ASTERISK) | (1 << CorpusQLParser.PLUS) | (1 << CorpusQLParser.QUESTION_MARK) | (1 << CorpusQLParser.LEFT_CURLY_BRACKET))) != 0):
                self.state = 73
                self.repetitionAmount()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(CorpusQLParser.LT, 0)

        def NAME(self):
            return self.getToken(CorpusQLParser.NAME, 0)

        def GT(self):
            return self.getToken(CorpusQLParser.GT, 0)

        def SOLIDUS(self, i:int=None):
            if i is None:
                return self.getTokens(CorpusQLParser.SOLIDUS)
            else:
                return self.getToken(CorpusQLParser.SOLIDUS, i)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CorpusQLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(CorpusQLParser.AttributeContext,i)


        def getRuleIndex(self):
            return CorpusQLParser.RULE_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag" ):
                listener.enterTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag" ):
                listener.exitTag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTag" ):
                return visitor.visitTag(self)
            else:
                return visitor.visitChildren(self)




    def tag(self):

        localctx = CorpusQLParser.TagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(CorpusQLParser.LT)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CorpusQLParser.SOLIDUS:
                self.state = 77
                self.match(CorpusQLParser.SOLIDUS)


            self.state = 80
            self.match(CorpusQLParser.NAME)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CorpusQLParser.NAME:
                self.state = 81
                self.attribute()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CorpusQLParser.SOLIDUS:
                self.state = 87
                self.match(CorpusQLParser.SOLIDUS)


            self.state = 90
            self.match(CorpusQLParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(CorpusQLParser.NAME, 0)

        def EQUALS(self):
            return self.getToken(CorpusQLParser.EQUALS, 0)

        def quotedString(self):
            return self.getTypedRuleContext(CorpusQLParser.QuotedStringContext,0)


        def getRuleIndex(self):
            return CorpusQLParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = CorpusQLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(CorpusQLParser.NAME)
            self.state = 93
            self.match(CorpusQLParser.EQUALS)
            self.state = 94
            self.quotedString()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PositionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CorpusQLParser.RULE_position

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PositionPositionWordContext(PositionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusQLParser.PositionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def positionWord(self):
            return self.getTypedRuleContext(CorpusQLParser.PositionWordContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositionPositionWord" ):
                listener.enterPositionPositionWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositionPositionWord" ):
                listener.exitPositionPositionWord(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositionPositionWord" ):
                return visitor.visitPositionPositionWord(self)
            else:
                return visitor.visitChildren(self)


    class PositionPositionLongContext(PositionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusQLParser.PositionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(CorpusQLParser.LEFT_SQUARE_BRACKET, 0)
        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(CorpusQLParser.RIGHT_SQUARE_BRACKET, 0)
        def positionLong(self):
            return self.getTypedRuleContext(CorpusQLParser.PositionLongContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositionPositionLong" ):
                listener.enterPositionPositionLong(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositionPositionLong" ):
                listener.exitPositionPositionLong(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositionPositionLong" ):
                return visitor.visitPositionPositionLong(self)
            else:
                return visitor.visitChildren(self)



    def position(self):

        localctx = CorpusQLParser.PositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_position)
        self._la = 0 # Token type
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CorpusQLParser.DOUBLE_QUOTED_STRING, CorpusQLParser.SINGLE_QUOTED_STRING]:
                localctx = CorpusQLParser.PositionPositionWordContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.positionWord()
                pass
            elif token in [CorpusQLParser.LEFT_SQUARE_BRACKET]:
                localctx = CorpusQLParser.PositionPositionLongContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.match(CorpusQLParser.LEFT_SQUARE_BRACKET)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CorpusQLParser.NAME) | (1 << CorpusQLParser.DOUBLE_QUOTED_STRING) | (1 << CorpusQLParser.SINGLE_QUOTED_STRING) | (1 << CorpusQLParser.LEFT_PARENTHESIS) | (1 << CorpusQLParser.EXCLAMATION_MARK))) != 0):
                    self.state = 98
                    self.positionLong()


                self.state = 101
                self.match(CorpusQLParser.RIGHT_SQUARE_BRACKET)
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


    class PositionWordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quotedString(self):
            return self.getTypedRuleContext(CorpusQLParser.QuotedStringContext,0)


        def getRuleIndex(self):
            return CorpusQLParser.RULE_positionWord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositionWord" ):
                listener.enterPositionWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositionWord" ):
                listener.exitPositionWord(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositionWord" ):
                return visitor.visitPositionWord(self)
            else:
                return visitor.visitChildren(self)




    def positionWord(self):

        localctx = CorpusQLParser.PositionWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_positionWord)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.quotedString()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PositionLongContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def positionLongPart(self):
            return self.getTypedRuleContext(CorpusQLParser.PositionLongPartContext,0)


        def booleanOperator(self):
            return self.getTypedRuleContext(CorpusQLParser.BooleanOperatorContext,0)


        def positionLong(self):
            return self.getTypedRuleContext(CorpusQLParser.PositionLongContext,0)


        def getRuleIndex(self):
            return CorpusQLParser.RULE_positionLong

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositionLong" ):
                listener.enterPositionLong(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositionLong" ):
                listener.exitPositionLong(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositionLong" ):
                return visitor.visitPositionLong(self)
            else:
                return visitor.visitChildren(self)




    def positionLong(self):

        localctx = CorpusQLParser.PositionLongContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_positionLong)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.positionLongPart()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CorpusQLParser.T__3) | (1 << CorpusQLParser.AMPERSAND) | (1 << CorpusQLParser.VERTICAL_LINE))) != 0):
                self.state = 107
                self.booleanOperator()
                self.state = 108
                self.positionLong()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PositionLongPartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attValuePair(self):
            return self.getTypedRuleContext(CorpusQLParser.AttValuePairContext,0)


        def LEFT_PARENTHESIS(self):
            return self.getToken(CorpusQLParser.LEFT_PARENTHESIS, 0)

        def positionLong(self):
            return self.getTypedRuleContext(CorpusQLParser.PositionLongContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(CorpusQLParser.RIGHT_PARENTHESIS, 0)

        def EXCLAMATION_MARK(self):
            return self.getToken(CorpusQLParser.EXCLAMATION_MARK, 0)

        def positionLongPart(self):
            return self.getTypedRuleContext(CorpusQLParser.PositionLongPartContext,0)


        def getRuleIndex(self):
            return CorpusQLParser.RULE_positionLongPart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositionLongPart" ):
                listener.enterPositionLongPart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositionLongPart" ):
                listener.exitPositionLongPart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositionLongPart" ):
                return visitor.visitPositionLongPart(self)
            else:
                return visitor.visitChildren(self)




    def positionLongPart(self):

        localctx = CorpusQLParser.PositionLongPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_positionLongPart)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.attValuePair()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(CorpusQLParser.LEFT_PARENTHESIS)
                self.state = 114
                self.positionLong()
                self.state = 115
                self.match(CorpusQLParser.RIGHT_PARENTHESIS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 117
                self.match(CorpusQLParser.EXCLAMATION_MARK)
                self.state = 118
                self.positionLongPart()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttValuePairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CorpusQLParser.RULE_attValuePair

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AttValuePairEqualsContext(AttValuePairContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusQLParser.AttValuePairContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def propName(self):
            return self.getTypedRuleContext(CorpusQLParser.PropNameContext,0)

        def EQUALS(self):
            return self.getToken(CorpusQLParser.EQUALS, 0)
        def valuePart(self):
            return self.getTypedRuleContext(CorpusQLParser.ValuePartContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttValuePairEquals" ):
                listener.enterAttValuePairEquals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttValuePairEquals" ):
                listener.exitAttValuePairEquals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttValuePairEquals" ):
                return visitor.visitAttValuePairEquals(self)
            else:
                return visitor.visitChildren(self)


    class AttValuePairNotEqualsContext(AttValuePairContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusQLParser.AttValuePairContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def propName(self):
            return self.getTypedRuleContext(CorpusQLParser.PropNameContext,0)

        def valuePart(self):
            return self.getTypedRuleContext(CorpusQLParser.ValuePartContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttValuePairNotEquals" ):
                listener.enterAttValuePairNotEquals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttValuePairNotEquals" ):
                listener.exitAttValuePairNotEquals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttValuePairNotEquals" ):
                return visitor.visitAttValuePairNotEquals(self)
            else:
                return visitor.visitChildren(self)


    class AttValuePairDefaultEqualsContext(AttValuePairContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusQLParser.AttValuePairContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def valuePart(self):
            return self.getTypedRuleContext(CorpusQLParser.ValuePartContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttValuePairDefaultEquals" ):
                listener.enterAttValuePairDefaultEquals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttValuePairDefaultEquals" ):
                listener.exitAttValuePairDefaultEquals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttValuePairDefaultEquals" ):
                return visitor.visitAttValuePairDefaultEquals(self)
            else:
                return visitor.visitChildren(self)



    def attValuePair(self):

        localctx = CorpusQLParser.AttValuePairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_attValuePair)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = CorpusQLParser.AttValuePairEqualsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.propName()
                self.state = 122
                self.match(CorpusQLParser.EQUALS)
                self.state = 123
                self.valuePart()
                pass

            elif la_ == 2:
                localctx = CorpusQLParser.AttValuePairNotEqualsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.propName()
                self.state = 126
                self.match(CorpusQLParser.T__1)
                self.state = 127
                self.valuePart()
                pass

            elif la_ == 3:
                localctx = CorpusQLParser.AttValuePairDefaultEqualsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.valuePart()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(CorpusQLParser.NAME)
            else:
                return self.getToken(CorpusQLParser.NAME, i)

        def SOLIDUS(self):
            return self.getToken(CorpusQLParser.SOLIDUS, 0)

        def getRuleIndex(self):
            return CorpusQLParser.RULE_propName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropName" ):
                listener.enterPropName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropName" ):
                listener.exitPropName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPropName" ):
                return visitor.visitPropName(self)
            else:
                return visitor.visitChildren(self)




    def propName(self):

        localctx = CorpusQLParser.PropNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_propName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(CorpusQLParser.NAME)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CorpusQLParser.SOLIDUS:
                self.state = 133
                self.match(CorpusQLParser.SOLIDUS)
                self.state = 134
                self.match(CorpusQLParser.NAME)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepetitionAmountContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CorpusQLParser.RULE_repetitionAmount

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RepetitionZeroOrMoreContext(RepetitionAmountContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusQLParser.RepetitionAmountContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ASTERISK(self):
            return self.getToken(CorpusQLParser.ASTERISK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepetitionZeroOrMore" ):
                listener.enterRepetitionZeroOrMore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepetitionZeroOrMore" ):
                listener.exitRepetitionZeroOrMore(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepetitionZeroOrMore" ):
                return visitor.visitRepetitionZeroOrMore(self)
            else:
                return visitor.visitChildren(self)


    class RepetitionMinMaxContext(RepetitionAmountContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusQLParser.RepetitionAmountContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEFT_CURLY_BRACKET(self):
            return self.getToken(CorpusQLParser.LEFT_CURLY_BRACKET, 0)
        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(CorpusQLParser.NUMBER)
            else:
                return self.getToken(CorpusQLParser.NUMBER, i)
        def LEFT_RIGHT_BRACKET(self):
            return self.getToken(CorpusQLParser.LEFT_RIGHT_BRACKET, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepetitionMinMax" ):
                listener.enterRepetitionMinMax(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepetitionMinMax" ):
                listener.exitRepetitionMinMax(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepetitionMinMax" ):
                return visitor.visitRepetitionMinMax(self)
            else:
                return visitor.visitChildren(self)


    class RepetitionExactlyContext(RepetitionAmountContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusQLParser.RepetitionAmountContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEFT_CURLY_BRACKET(self):
            return self.getToken(CorpusQLParser.LEFT_CURLY_BRACKET, 0)
        def NUMBER(self):
            return self.getToken(CorpusQLParser.NUMBER, 0)
        def LEFT_RIGHT_BRACKET(self):
            return self.getToken(CorpusQLParser.LEFT_RIGHT_BRACKET, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepetitionExactly" ):
                listener.enterRepetitionExactly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepetitionExactly" ):
                listener.exitRepetitionExactly(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepetitionExactly" ):
                return visitor.visitRepetitionExactly(self)
            else:
                return visitor.visitChildren(self)


    class RepetitionZeroOrOneContext(RepetitionAmountContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusQLParser.RepetitionAmountContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def QUESTION_MARK(self):
            return self.getToken(CorpusQLParser.QUESTION_MARK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepetitionZeroOrOne" ):
                listener.enterRepetitionZeroOrOne(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepetitionZeroOrOne" ):
                listener.exitRepetitionZeroOrOne(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepetitionZeroOrOne" ):
                return visitor.visitRepetitionZeroOrOne(self)
            else:
                return visitor.visitChildren(self)


    class RepetitionOneOrMoreContext(RepetitionAmountContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusQLParser.RepetitionAmountContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(CorpusQLParser.PLUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepetitionOneOrMore" ):
                listener.enterRepetitionOneOrMore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepetitionOneOrMore" ):
                listener.exitRepetitionOneOrMore(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepetitionOneOrMore" ):
                return visitor.visitRepetitionOneOrMore(self)
            else:
                return visitor.visitChildren(self)



    def repetitionAmount(self):

        localctx = CorpusQLParser.RepetitionAmountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_repetitionAmount)
        self._la = 0 # Token type
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = CorpusQLParser.RepetitionZeroOrMoreContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(CorpusQLParser.ASTERISK)
                pass

            elif la_ == 2:
                localctx = CorpusQLParser.RepetitionOneOrMoreContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(CorpusQLParser.PLUS)
                pass

            elif la_ == 3:
                localctx = CorpusQLParser.RepetitionZeroOrOneContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.match(CorpusQLParser.QUESTION_MARK)
                pass

            elif la_ == 4:
                localctx = CorpusQLParser.RepetitionExactlyContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 140
                self.match(CorpusQLParser.LEFT_CURLY_BRACKET)
                self.state = 141
                self.match(CorpusQLParser.NUMBER)
                self.state = 142
                self.match(CorpusQLParser.LEFT_RIGHT_BRACKET)
                pass

            elif la_ == 5:
                localctx = CorpusQLParser.RepetitionMinMaxContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 143
                self.match(CorpusQLParser.LEFT_CURLY_BRACKET)
                self.state = 144
                self.match(CorpusQLParser.NUMBER)
                self.state = 145
                self.match(CorpusQLParser.T__2)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CorpusQLParser.NUMBER:
                    self.state = 146
                    self.match(CorpusQLParser.NUMBER)


                self.state = 149
                self.match(CorpusQLParser.LEFT_RIGHT_BRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuotedStringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE_QUOTED_STRING(self):
            return self.getToken(CorpusQLParser.DOUBLE_QUOTED_STRING, 0)

        def SINGLE_QUOTED_STRING(self):
            return self.getToken(CorpusQLParser.SINGLE_QUOTED_STRING, 0)

        def getRuleIndex(self):
            return CorpusQLParser.RULE_quotedString

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuotedString" ):
                listener.enterQuotedString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuotedString" ):
                listener.exitQuotedString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuotedString" ):
                return visitor.visitQuotedString(self)
            else:
                return visitor.visitChildren(self)




    def quotedString(self):

        localctx = CorpusQLParser.QuotedStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_quotedString)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            _la = self._input.LA(1)
            if not(_la==CorpusQLParser.DOUBLE_QUOTED_STRING or _la==CorpusQLParser.SINGLE_QUOTED_STRING):
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


    class BooleanOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CorpusQLParser.RULE_booleanOperator

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OrContext(BooleanOperatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusQLParser.BooleanOperatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VERTICAL_LINE(self):
            return self.getToken(CorpusQLParser.VERTICAL_LINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(BooleanOperatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusQLParser.BooleanOperatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def AMPERSAND(self):
            return self.getToken(CorpusQLParser.AMPERSAND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class ImplicationContext(BooleanOperatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusQLParser.BooleanOperatorContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplication" ):
                listener.enterImplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplication" ):
                listener.exitImplication(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplication" ):
                return visitor.visitImplication(self)
            else:
                return visitor.visitChildren(self)



    def booleanOperator(self):

        localctx = CorpusQLParser.BooleanOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_booleanOperator)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CorpusQLParser.AMPERSAND]:
                localctx = CorpusQLParser.AndContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(CorpusQLParser.AMPERSAND)
                pass
            elif token in [CorpusQLParser.VERTICAL_LINE]:
                localctx = CorpusQLParser.OrContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(CorpusQLParser.VERTICAL_LINE)
                pass
            elif token in [CorpusQLParser.T__3]:
                localctx = CorpusQLParser.ImplicationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.match(CorpusQLParser.T__3)
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


    class ValuePartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CorpusQLParser.RULE_valuePart

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ValuePartStringContext(ValuePartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusQLParser.ValuePartContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def quotedString(self):
            return self.getTypedRuleContext(CorpusQLParser.QuotedStringContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValuePartString" ):
                listener.enterValuePartString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValuePartString" ):
                listener.exitValuePartString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValuePartString" ):
                return visitor.visitValuePartString(self)
            else:
                return visitor.visitChildren(self)


    class ValuePartParenthesisedContext(ValuePartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusQLParser.ValuePartContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEFT_PARENTHESIS(self):
            return self.getToken(CorpusQLParser.LEFT_PARENTHESIS, 0)
        def value(self):
            return self.getTypedRuleContext(CorpusQLParser.ValueContext,0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(CorpusQLParser.RIGHT_PARENTHESIS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValuePartParenthesised" ):
                listener.enterValuePartParenthesised(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValuePartParenthesised" ):
                listener.exitValuePartParenthesised(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValuePartParenthesised" ):
                return visitor.visitValuePartParenthesised(self)
            else:
                return visitor.visitChildren(self)



    def valuePart(self):

        localctx = CorpusQLParser.ValuePartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_valuePart)
        try:
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CorpusQLParser.DOUBLE_QUOTED_STRING, CorpusQLParser.SINGLE_QUOTED_STRING]:
                localctx = CorpusQLParser.ValuePartStringContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.quotedString()
                pass
            elif token in [CorpusQLParser.LEFT_PARENTHESIS]:
                localctx = CorpusQLParser.ValuePartParenthesisedContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.match(CorpusQLParser.LEFT_PARENTHESIS)
                self.state = 161
                self.value()
                self.state = 162
                self.match(CorpusQLParser.RIGHT_PARENTHESIS)
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


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CorpusQLParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ValueWithoutContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusQLParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def valuePart(self):
            return self.getTypedRuleContext(CorpusQLParser.ValuePartContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueWithout" ):
                listener.enterValueWithout(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueWithout" ):
                listener.exitValueWithout(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValueWithout" ):
                return visitor.visitValueWithout(self)
            else:
                return visitor.visitChildren(self)


    class ValueWithContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusQLParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def valuePart(self):
            return self.getTypedRuleContext(CorpusQLParser.ValuePartContext,0)

        def booleanOperator(self):
            return self.getTypedRuleContext(CorpusQLParser.BooleanOperatorContext,0)

        def value(self):
            return self.getTypedRuleContext(CorpusQLParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueWith" ):
                listener.enterValueWith(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueWith" ):
                listener.exitValueWith(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValueWith" ):
                return visitor.visitValueWith(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = CorpusQLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_value)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                localctx = CorpusQLParser.ValueWithContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.valuePart()
                self.state = 167
                self.booleanOperator()
                self.state = 168
                self.value()
                pass

            elif la_ == 2:
                localctx = CorpusQLParser.ValueWithoutContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.valuePart()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





