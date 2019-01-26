from Node import *
from Token import *


class LALRTreeBuilder:
    def __init__(self, table, productions):
        self.table = table
        self.productions = productions

    def builder(self):
        def build(tokens):
            self.build_inner(tokens)

        return build

    def build_inner(self, tokens):
        tokens.append(Token('$', '', (0, 0), (0, 0)))
        stack = ['0']
        lookahead = tokens[0]
        while True:
            state = stack.pop()
            action = self.table[state]['ACTION']
            pass



