from node import *
from lexer import *


class Point:
    def __init__(self, left, right, pos, lookahead):
        self.left = left
        self.right = right
        self.pos = pos
        self.lookahead = lookahead


class Condition:
    def __init__(self, points):
        self.points = points

    def closure(self, nt, t, rules, first):
        flag = True

        def find_first(next_token, lookahead):
            if next_token is None:
                return [lookahead]
            if next_token in t:
                return [t]
            if next_token in nt:
                return first[next_token]
            raise Exception('No matches found in is_first function')


        while(flag):
            # Фильтруем, чтобы позиция стояла у нетерминала
            filtered_points = list(filter(lambda x: x.right[x.pos] in nt, self.points))
            for p in filtered_points:

                production_nt = p.right[p.pos]
                productions = rules[production_nt]

                for prod in productions:
                    next_token = None
                    if (len(p.right) - 1 > p.pos):
                        next_token = p.right[p.pos + 1]

                    firsts = find_first(next_token, p.lookahead)

                    for f in firsts:
                        self.points.append(Point(production_nt, prod, 0, f))

                    if len(firsts) == 0:
                        flag = False


def goto(point, symbol):


    pass

def build_lalr_ctx(axiom, terminals, non_terminals, rules, first):
    non_terminals.add('~S~')
    rules['~S~'] = [[axiom]]

    initial_point = Point('~S~', [axiom], 0, '$'),
    initial_cond = Condition(list(initial_point))

    initial_cond.closure(non_terminals, terminals, rules, first)

    pass
