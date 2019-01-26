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
        index = 0
        lookahead = tokens[0]
        while True:
            state = stack[len(stack) - 1]
            action = self.table[state]['ACTION'][lookahead.domain]
            if action[0] == 's':
                stack.append(action[1:])
                index += 1
                lookahead = tokens[index]

            if action[0] == 'r':
                production_idx = int(action[1:])
                production = self.productions[production_idx]
                rule = production['right']
                stack = stack[:len(stack) - len(production['right'])]
                state = stack[0]
                stack.append(self.table[state]['GOTO'][production['left']])


