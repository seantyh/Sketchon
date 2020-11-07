# Generated from /Users/seantyh/langon/Sketchon/dep/../src/sketchon/cql_parser/CorpusQL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\36")
        buf.write("\u00b0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\7\b^\n\b\f\b\16\ba\13\b\3")
        buf.write("\t\6\td\n\t\r\t\16\te\3\n\3\n\3\n\7\nk\n\n\f\n\16\nn\13")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13v\n\13\3\f\3\f\3\f")
        buf.write("\7\f{\n\f\f\f\16\f~\13\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u0086")
        buf.write("\n\r\3\16\6\16\u0089\n\16\r\16\16\16\u008a\3\16\3\16\3")
        buf.write("\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24")
        buf.write("\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\4l|\2 \3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\2\27\f\31\2\33\r\35\16\37\17!\20#\21%\22\'\23)\24")
        buf.write("+\25-\26/\27\61\30\63\31\65\32\67\339\34;\35=\36\3\2\6")
        buf.write("\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\5\2\13\f\17\17\"\"")
        buf.write("\2\u00b6\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\27\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\3?\3\2\2\2\5A\3\2\2\2\7D\3\2")
        buf.write("\2\2\tF\3\2\2\2\13I\3\2\2\2\rP\3\2\2\2\17[\3\2\2\2\21")
        buf.write("c\3\2\2\2\23g\3\2\2\2\25u\3\2\2\2\27w\3\2\2\2\31\u0085")
        buf.write("\3\2\2\2\33\u0088\3\2\2\2\35\u008e\3\2\2\2\37\u0090\3")
        buf.write("\2\2\2!\u0092\3\2\2\2#\u0094\3\2\2\2%\u0096\3\2\2\2\'")
        buf.write("\u0098\3\2\2\2)\u009a\3\2\2\2+\u009c\3\2\2\2-\u009e\3")
        buf.write("\2\2\2/\u00a0\3\2\2\2\61\u00a2\3\2\2\2\63\u00a4\3\2\2")
        buf.write("\2\65\u00a6\3\2\2\2\67\u00a8\3\2\2\29\u00aa\3\2\2\2;\u00ac")
        buf.write("\3\2\2\2=\u00ae\3\2\2\2?@\7<\2\2@\4\3\2\2\2AB\7#\2\2B")
        buf.write("C\7?\2\2C\6\3\2\2\2DE\7.\2\2E\b\3\2\2\2FG\7/\2\2GH\7@")
        buf.write("\2\2H\n\3\2\2\2IJ\7Y\2\2JK\7K\2\2KL\7V\2\2LM\7J\2\2MN")
        buf.write("\7K\2\2NO\7P\2\2O\f\3\2\2\2PQ\7E\2\2QR\7Q\2\2RS\7P\2\2")
        buf.write("ST\7V\2\2TU\7C\2\2UV\7K\2\2VW\7P\2\2WX\7K\2\2XY\7P\2\2")
        buf.write("YZ\7I\2\2Z\16\3\2\2\2[_\t\2\2\2\\^\t\3\2\2]\\\3\2\2\2")
        buf.write("^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`\20\3\2\2\2a_\3\2\2\2b")
        buf.write("d\t\4\2\2cb\3\2\2\2de\3\2\2\2ec\3\2\2\2ef\3\2\2\2f\22")
        buf.write("\3\2\2\2gl\7$\2\2hk\5\25\13\2ik\13\2\2\2jh\3\2\2\2ji\3")
        buf.write("\2\2\2kn\3\2\2\2lm\3\2\2\2lj\3\2\2\2mo\3\2\2\2nl\3\2\2")
        buf.write("\2op\7$\2\2p\24\3\2\2\2qr\7^\2\2rv\7$\2\2st\7^\2\2tv\7")
        buf.write("^\2\2uq\3\2\2\2us\3\2\2\2v\26\3\2\2\2w|\7)\2\2x{\5\31")
        buf.write("\r\2y{\13\2\2\2zx\3\2\2\2zy\3\2\2\2{~\3\2\2\2|}\3\2\2")
        buf.write("\2|z\3\2\2\2}\177\3\2\2\2~|\3\2\2\2\177\u0080\7)\2\2\u0080")
        buf.write("\30\3\2\2\2\u0081\u0082\7^\2\2\u0082\u0086\7)\2\2\u0083")
        buf.write("\u0084\7^\2\2\u0084\u0086\7^\2\2\u0085\u0081\3\2\2\2\u0085")
        buf.write("\u0083\3\2\2\2\u0086\32\3\2\2\2\u0087\u0089\t\5\2\2\u0088")
        buf.write("\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u0088\3\2\2\2")
        buf.write("\u008a\u008b\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d\b")
        buf.write("\16\2\2\u008d\34\3\2\2\2\u008e\u008f\7>\2\2\u008f\36\3")
        buf.write("\2\2\2\u0090\u0091\7@\2\2\u0091 \3\2\2\2\u0092\u0093\7")
        buf.write("\61\2\2\u0093\"\3\2\2\2\u0094\u0095\7?\2\2\u0095$\3\2")
        buf.write("\2\2\u0096\u0097\7]\2\2\u0097&\3\2\2\2\u0098\u0099\7_")
        buf.write("\2\2\u0099(\3\2\2\2\u009a\u009b\7*\2\2\u009b*\3\2\2\2")
        buf.write("\u009c\u009d\7+\2\2\u009d,\3\2\2\2\u009e\u009f\7#\2\2")
        buf.write("\u009f.\3\2\2\2\u00a0\u00a1\7,\2\2\u00a1\60\3\2\2\2\u00a2")
        buf.write("\u00a3\7-\2\2\u00a3\62\3\2\2\2\u00a4\u00a5\7A\2\2\u00a5")
        buf.write("\64\3\2\2\2\u00a6\u00a7\7}\2\2\u00a7\66\3\2\2\2\u00a8")
        buf.write("\u00a9\7\177\2\2\u00a98\3\2\2\2\u00aa\u00ab\7(\2\2\u00ab")
        buf.write(":\3\2\2\2\u00ac\u00ad\7~\2\2\u00ad<\3\2\2\2\u00ae\u00af")
        buf.write("\7/\2\2\u00af>\3\2\2\2\f\2_ejluz|\u0085\u008a\3\b\2\2")
        return buf.getvalue()


class CorpusQLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    WITHIN = 5
    CONTAINING = 6
    NAME = 7
    NUMBER = 8
    DOUBLE_QUOTED_STRING = 9
    SINGLE_QUOTED_STRING = 10
    WS = 11
    LT = 12
    GT = 13
    SOLIDUS = 14
    EQUALS = 15
    LEFT_SQUARE_BRACKET = 16
    RIGHT_SQUARE_BRACKET = 17
    LEFT_PARENTHESIS = 18
    RIGHT_PARENTHESIS = 19
    EXCLAMATION_MARK = 20
    ASTERISK = 21
    PLUS = 22
    QUESTION_MARK = 23
    LEFT_CURLY_BRACKET = 24
    LEFT_RIGHT_BRACKET = 25
    AMPERSAND = 26
    VERTICAL_LINE = 27
    HYPHEN_MINUS = 28

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'!='", "','", "'->'", "'WITHIN'", "'CONTAINING'", "'<'", 
            "'>'", "'/'", "'='", "'['", "']'", "'('", "')'", "'!'", "'*'", 
            "'+'", "'?'", "'{'", "'}'", "'&'", "'|'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "WITHIN", "CONTAINING", "NAME", "NUMBER", "DOUBLE_QUOTED_STRING", 
            "SINGLE_QUOTED_STRING", "WS", "LT", "GT", "SOLIDUS", "EQUALS", 
            "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "LEFT_PARENTHESIS", 
            "RIGHT_PARENTHESIS", "EXCLAMATION_MARK", "ASTERISK", "PLUS", 
            "QUESTION_MARK", "LEFT_CURLY_BRACKET", "LEFT_RIGHT_BRACKET", 
            "AMPERSAND", "VERTICAL_LINE", "HYPHEN_MINUS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "WITHIN", "CONTAINING", 
                  "NAME", "NUMBER", "DOUBLE_QUOTED_STRING", "DOUBLE_QUOTED_ESC", 
                  "SINGLE_QUOTED_STRING", "SINGLE_QUOTED_ESC", "WS", "LT", 
                  "GT", "SOLIDUS", "EQUALS", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
                  "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "EXCLAMATION_MARK", 
                  "ASTERISK", "PLUS", "QUESTION_MARK", "LEFT_CURLY_BRACKET", 
                  "LEFT_RIGHT_BRACKET", "AMPERSAND", "VERTICAL_LINE", "HYPHEN_MINUS" ]

    grammarFileName = "CorpusQL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


