from Node import *
from Token import *


class LALRTreeBuilder:
    def __init__(self, table, productions):
        self.table = table
        self.productions = productions

    def builder(self):
        def build(tokens):
            return self.build_inner(tokens)

        return build

    def build_inner(self, tokens):
        tokens.append(Token('$', '', (0, 0), (0, 0)))
        stack = ['0']
        next = tokens[0]
        buffer = list()

        while True:
            state = stack[len(stack) - 1]
            action = self.table[state]['ACTION'][next.domain]
            if action[0] == 's':
                stack.append(action[1:])
                buffer.append(Node.from_token(next, list()))
                tokens = tokens[1:]
                next = tokens[0]

            if action[0] == 'r':
                production_idx = int(action[1:])
                production = self.productions[production_idx]
                rule = production['right']
                stack = stack[:len(stack) - len(rule)]
                state = stack[len(stack) - 1]
                stack.append(self.table[state]['GOTO'][production['left']])
                children = buffer[len(buffer) - len(rule):]
                buffer = buffer[:len(buffer) - len(rule)]

                new_node = Node(production['left'], list(), None)
                for i in children:
                    new_node.add_child(i)

                buffer.append(new_node)

            if action == 'acc':
                break

        return buffer[0]
