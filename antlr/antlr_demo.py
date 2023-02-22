# Copyright 2023 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from expr_parser import ExprLexer, ExprListener, ExprParser  # pants: no-infer-dep


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
