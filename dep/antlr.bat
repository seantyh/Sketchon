java -Xmx500M ^
    -cp "./antlr-4.9.1-complete.jar" ^
    org.antlr.v4.Tool ^
    -Dlanguage=Python3 ^
    ../src/sketchon/cql_parser/CorpusQL.g4 ^
    -visitor
