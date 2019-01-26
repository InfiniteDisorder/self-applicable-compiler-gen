from Node import *
from GrammarLexer import *

def build_tree(tokens, T, NT, table, axiom):
    tokens.append(Token('$', '', (0, 0), (0, 0)))
    tree = None
    stack = [('$', None), (axiom, None)]
    a = tokens[0]
    while True:
        x = stack[-1]
        if x[0] != '$':
            if x[0] in T:
                if a.domain == x[0]:
                    x[1].add_child(Node(a, [], x[1]))
                    stack.pop()
                    tokens = tokens[1:]
                    a = tokens[0]
                else:
                    print('An error occurred at:', str(a))
                    break
            elif x[0] in NT:
                try:
                    rule = table[x[0]][a.domain]
                    stack.pop()
                    new_node = Node(x[0], [], x[1])
                    if not x[1]:
                        tree = new_node
                    else:
                        x[1].add_child(new_node)

                    for i in reversed(rule):
                        if i != '':
                            stack.append((i, new_node))

                except KeyError:
                    print('ERROR')
                    break
        else:
            break

    return tree

