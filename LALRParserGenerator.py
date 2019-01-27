from self_lalr_table import *
from LALR import *
from LALRTreeBuilder import *
from GrammarLexer import Lexer

class LALRParserGenerator:
    def __init__(self, program):
        build = LALRTreeBuilder(table, productions).builder()
        self.tree = build(Lexer(program).analyze())
        pass

