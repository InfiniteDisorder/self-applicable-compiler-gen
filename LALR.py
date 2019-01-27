class Production:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def cmp_point(self, point):
        return self.left == point.left and self.right == point.right

    def __str__(self):
        right = ', '.join(map(lambda x: f'\'{x}\'', self.right))
        return '{' + f'\'left\': \'{self.left}\', \'right\': [{right}]' + '}'


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


def compare_kernels(p1, p2):
    if p1.left == p2.left and \
        p1.right == p2.right and \
        p1.pos == p2.pos:
        return True

    return False


class State:
    def __init__(self, points, nt):
        self.points = points
        self.name = None
        self.kernel = list(points)
        self.goto_dict = {}
        self.action = {}
        self.nt = nt
        self.closured = False

    def set_name(self, name):
        self.name = name

    def already_has_point(self, p):
        return any(map(lambda x: compare(x, p), self.points))

    def closure(self, nt, t, rules, first):
        flag = True

        def find_first(next_token, lookahead):
            if next_token is None:
                if lookahead == '':
                    return list(['$'])
                else:
                    return list([lookahead])
            if next_token in t:
                if next_token == '':
                    pass
                return list([next_token])
            if next_token in nt:
                if '' in first[next_token]:
                    res = set(first[next_token])
                    res.discard('')
                    res.add(lookahead)
                    return list(sorted(res))

                return first[next_token]
            raise Exception('No matches found in is_first function')

        while flag:
            # filtering points with following non-terminal
            filtered_points = list(filter(lambda x: len(x.right) > x.pos and x.right[x.pos] in nt, self.points))
            if len(filtered_points) == 0:
                flag = False

            prev_len = len(self.points)

            for p in filtered_points:

                production_nt = p.right[p.pos]
                productions = rules[production_nt]

                for prod in productions:
                    next_token = None
                    if len(p.right) - 1 > p.pos:
                        next_token = p.right[p.pos + 1]

                    firsts = find_first(next_token, p.lookahead)

                    for f in firsts:
                        new_point = Point(production_nt, prod, 0, f)
                        if not self.already_has_point(new_point):

                            self.points.append(new_point)

            if prev_len == len(self.points):
                flag = False

        self.closured = True

    def goto(self, token, nt, t, rules, first):
        new_points = list()

        for i in self.points:
            if token == 'n' and i.left == 'F':
                token = token

            if len(i.right) > i.pos and i.right[i.pos] == token:
                new_points.append(Point(i.left, i.right, i.pos + 1, i.lookahead))

        new_state = State(new_points, nt)
        new_state.closure(nt, t, rules, first)

        return new_state

    def __str__(self):
        action = '\t\t\'ACTION\': {\n' + ',\n'.join(map(lambda k: f'\t\t\t\'{k}\': \'{self.action[k]}\'', self.action)) + \
                 '\n\t\t}'

        goto = '\t\t\'GOTO\': {\n' + ',\n'.join(map(lambda k: f'\t\t\t\'{k}\': \'{self.goto_dict[k]}\'', self.goto_dict)) + \
               '\n\t\t}'
        return '{\n' + action + ',\n' + goto + '\n\t}'


def compare_point_sets_partial(set_a, set_b):
    return all(
        map(lambda y:
            any(
                map(lambda x: compare(x, y), set_a),
            ),
            set_b
            )
    )


def compare_point_sets(set_a, set_b):
    return compare_point_sets_partial(set_a, set_b) and compare_point_sets_partial(set_b, set_a)


def compare_kernel_sets_partial(set_a, set_b):
    return all(
        map(lambda y:
            any(
                map(lambda x: compare_kernels(x, y), set_a),
            ),
            set_b
            )
    )


def compare_kernel_sets(set_a, set_b):
    return compare_kernel_sets_partial(set_a, set_b) and compare_kernel_sets_partial(set_b, set_a)


class LALRStateMachine:
    def __init__(self, axiom, terminals, non_terminals, rules, first):
        non_terminals.add('~S~')
        rules['~S~'] = [[axiom]]

        initial_point = Point('~S~', [axiom], 0, '$'),
        initial_state = State(list(initial_point), non_terminals)

        initial_state.closure(non_terminals, terminals, rules, first)

        states = list()
        states.append(initial_state)
        initial_state.set_name(0)

        counter = 1
        flag = True

        ext_terminals = set(terminals)
        ext_terminals.add('$')

        while flag:
            flag = False
            for i in set(states):
                for symbol in ext_terminals.union(non_terminals):
                    f = i.goto(symbol, non_terminals, terminals, rules, first)
                    if symbol == 'n':
                        symbol = symbol
                    if len(f.points) != 0 and not any(map(lambda x: compare_point_sets(x.points, f.points), states)):
                        flag = True
                        states.append(f)
                        f.set_name(counter)
                        counter += 1
                        i.goto_dict[symbol] = f.name

                    else:
                        m = list(filter(lambda x: compare_point_sets(x.points, f.points), states))
                        assert len(m) <= 1
                        if len(m) == 1:
                            i.goto_dict[symbol] = m[0].name

        # states with union kernels

        lalr_states = list()
        for i in states:
            kernel = list(i.kernel)
            name = list([i.name])
            for j in states:
                if j != i:
                    if compare_kernel_sets(j.kernel, i.kernel):
                        kernel = list(set(kernel).union(set(j.kernel)))
                        name.append(j.name)

            new_state = State(kernel, non_terminals)
            if not any(map(lambda x: compare_point_sets(x.points, new_state.points), lalr_states)):
                lalr_states.append(new_state)
                new_state.name = '_'.join(map(lambda x: str(x), sorted(name)))
                new_state.union_of = list(name)

        a = sum(map(lambda x: len(x.union_of), lalr_states))
        b = len(states)

        assert a == b

        productions = list()

        for h in rules:
            for r in rules[h]:
                productions.append(Production(h, r))

        for i in states:
            for symbol in ext_terminals.union(non_terminals):
                if symbol in i.goto_dict:
                    shift = i.goto_dict[symbol]
                    union_state_1 = list(filter(lambda x: i.name in x.union_of, lalr_states))[0]
                    union_state_2 = list(filter(lambda x: shift in x.union_of, lalr_states))[0]
                    union_state_1.goto_dict[symbol] = union_state_2.name

        for j in lalr_states:
            j.closure(non_terminals, terminals, rules, first)

        for j in lalr_states:
            for p in j.points:
                if len(p.right) > p.pos:
                    lookahead = p.right[p.pos]
                    if lookahead in ext_terminals and lookahead in j.goto_dict:
                        j.action[lookahead] = 's' + j.goto_dict[lookahead]

                elif len(p.right) == p.pos and p.left != '~S~':
                    indices = [i for i, el in enumerate(productions) if el.cmp_point(p)]
                    assert len(indices) == 1
                    j.action[p.lookahead] = 'r' + str(indices[0])

                elif compare(Point('~S~', [axiom], 1, '$'), p):
                    j.action['$'] = 'acc'

                else:
                    raise Exception('Provided grammar is not LALR(1) parseable')

        self.productions = productions
        self.states = lalr_states

        # for i in states:
        #     print(i.name)
        #     print(i.goto_dict)
        #     for j in i.kernel:
        #         print(j.left, '->', j.right, ':', j.pos, ',', j.lookahead)

        # for i in lalr_states:
        #     print(i.name)
        #     print(i.goto_dict)
        #     for j in i.points:
        #         print(j.left, '->', j.right, ':', j.pos, ',', j.lookahead)

        for i in lalr_states:
            assert len(i.goto_dict) != 0 or len(i.action) != 0
            assert len(i.action) != 0
            for k in i.goto_dict:
                if k in ext_terminals:
                    assert k in i.action

    def __str__(self):
        self.print_states()
        return self.print_productions() + '\n\n' + self.print_states() + '\n'

    def print_productions(self):
        prd = ',\n'.join(map(lambda x: '\t' + str(x), self.productions))
        return f'productions = [\n{prd}\n]'

    def print_states(self):
        table = '{\n' + ',\n'.join(map(lambda x: f'\t\'{x.name}\': {str(x)}', self.states)) + '\n}'
        return f'table = {table}'

    def to_file(self, name):
        f = open(name, 'w')
        f.write(str(self))




