from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from expr_parser import ExprLexer, ExprParser, ExprListener # pants: no-infer-dep

class ExprPrinter(ExprListener.ExprListener):     
    def exitExpr(self, ctx):         
        print(f"expr: {ctx.getText()=}") 


lexer = ExprLexer.ExprLexer(InputStream("10+20+30\n"))
token_stream = CommonTokenStream(lexer)
parser = ExprParser.ExprParser(token_stream)
tree = parser.prog()
printer = ExprPrinter()
walker = ParseTreeWalker()
walker.walk(printer, tree)
