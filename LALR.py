from node import *
from lexer import *


class Point:
    def __init__(self, left, right, pos, lookahead):
        self.left = left
        self.right = right
        self.pos = pos
        self.lookahead = lookahead

    def __cmp__(self, other):
        if self.left == other.left and \
           self.right == other.right and \
           self.pos == other.pos and \
           self.lookahead == other.lookahead:
            return 0
        return -1


def compare(p1, p2):
    if p1.left == p2.left and \
        p1.right == p2.right and \
        p1.pos == p2.pos and \
        p1.lookahead == p2.lookahead:
        return True

    return False

class State:
    def __init__(self, points):
        self.points = points

    def already_has_point(self, p):
        return any(map(lambda x: compare(x, p), self.points))


    def closure(self, nt, t, rules, first):
        flag = True

        def find_first(next_token, lookahead):
            if next_token is None:
                if lookahead == '':
                    return list('$')
                else:
                    return list(lookahead)
            if next_token in t:
                if next_token == '':
                    pass
                return list(next_token)
            if next_token in nt:
                return first[next_token]
            raise Exception('No matches found in is_first function')


        while(flag):
            # Фильтруем, чтобы позиция стояла у нетерминала
            filtered_points = list(filter(lambda x: len(x.right) > x.pos and x.right[x.pos] in nt, self.points))
            if len(filtered_points) == 0:
                flag = False

            for p in filtered_points:

                production_nt = p.right[p.pos]
                productions = rules[production_nt]

                for prod in productions:
                    next_token = None
                    if len(p.right) - 1 > p.pos:
                        next_token = p.right[p.pos + 1]

                    firsts = find_first(next_token, p.lookahead)

                    prev_len = len(self.points)

                    for f in firsts:
                        new_point = Point(production_nt, prod, 0, f)
                        if not self.already_has_point(new_point):

                            self.points.add(new_point)

                    if prev_len == len(self.points):
                        flag = False

    def goto(self, token, nt, t, rules, first):
        new_points = set()

        for i in self.points:
            if len(i.right) > i.pos and i.right[i.pos] == token:
                new_points.add(Point(i.left, i.right, i.pos + 1, i.lookahead))

        new_state = State(new_points)
        new_state.closure(nt, t, rules, first)

        return new_state


def compare_point_sets(set_a, set_b):
    return all(
        map(lambda y:
            any(
                map(lambda x: compare(x, y), set_a),
            ),
            set_b
        )
    )

def build_lalr_ctx(axiom, terminals, non_terminals, rules, first):
    non_terminals.add('~S~')
    rules['~S~'] = [[axiom]]

    initial_point = Point('~S~', [axiom], 0, '$'),
    initial_state = State(set(initial_point))

    initial_state.closure(non_terminals, terminals, rules, first)

    states = set()
    states.add(initial_state)

    flag = True
    while flag:
        flag = False
        for i in set(states):
            for symbol in non_terminals.union(terminals):
                f = i.goto(symbol, non_terminals, terminals, rules, first)
                if len(f.points) != 0 and not any(map(lambda x: compare_point_sets(x.points, f.points), states)):
                    flag = True
                    states.add(f)
    pass
