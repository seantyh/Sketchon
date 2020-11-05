from .cql_parser import CqlParserVisitor

class CqlQuery(CqlParserVisitor):
    def __init__(self, text):
        pass

    def visitRoot(self, ctx):
        print("visitRoot")
        print(ctx)