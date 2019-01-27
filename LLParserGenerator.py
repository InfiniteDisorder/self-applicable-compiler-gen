from self_table import *
from LLTreeBuilder import *
from LALR import *


class LLParserGenerator(object):
    def __init__(self, program):
        self.lexer = Lexer(program)
        self.tree = []
        self.T = self_table_TL
        self.NT = self_table_NTL
        self.predict_analysis_table = self_table
        self.TL = set()
        self.NTL = set()
        self.rules = []
        self.axiom = None
        self.first = {}
        self.follow = {}
        self.parser_table = {}
        self.tree = build_tree(self.lexer.analyze(), self.T, self.NT, self.predict_analysis_table, 'P')
        self.analyze_inner_tree()
        self.create_first_sets()
        self.state_machine = LALRStateMachine(self.axiom, self.TL, self.NTL, self.rules, self.first)

        # self.create_follow_sets()
        # self.create_parser_table()
        # print(self.first)
        # print(self.follow)
        # for i in self.parser_table:
        #     print(i, self.parser_table[i])

    def first_walk(self, node):
        if node.marker == 'P':
            for c in node.children:
                self.first_walk(c)
        elif node.marker == 'TD':
            ident = node.children[1]
            if ident.marker.image[1:-1] in self.TL:
                print('ERROR: duplicate token declaration.')
            else:
                pass
                #print(ident.marker.image[1:-1])
            self.TL.add(ident.marker.image[1:-1])
            self.first_walk(node.children[2])
        elif node.marker == 'CI' and node.children:
            ident = node.children[1]
            if ident.marker.image[1:-1] in self.TL:
                print('ERROR: duplicate token declaration.')
            else:
                pass
                #print(ident.marker.image[1:-1])
            self.TL.add(ident.marker.image[1:-1])
            self.first_walk(node.children[2])
        elif node.marker == 'RD':
            ident = node.children[0]
            self.NTL.add(ident.marker.image[1:-1])

    def second_walk(self, node):
        if node.marker == 'P':
            if node.children:
                if isinstance(node.children[0].marker, Token) and node.children[0].marker.domain == 'ST':
                    ident = node.children[1]
                    if not self.axiom:
                        self.axiom = ident.marker.image[1:-1]
                        self.second_walk(node.children[3])
                    else:
                        print('ERROR: the axiom was previously declared.')
                else:
                    for c in node.children:
                        self.second_walk(c)

        elif node.marker == 'RD':
            ident = node.children[0]
            rule_rhs = []
            s_node = node.children[2]
            while s_node.children:
                s_ident = s_node.children[0]
                if s_ident.marker.image[1:-1] in self.TL or s_ident.marker.image[1:-1] in self.NTL:
                    rule_rhs.append(s_ident.marker.image[1:-1])
                else:
                    print('ERROR: unknown non-terminal symbol', s_ident.marker.image[1:-1])
                s_node = s_node.children[1]
            self.rules[ident.marker.image[1:-1]].append(rule_rhs)

    def analyze_inner_tree(self):
        self.first_walk(self.tree)
        self.rules = {x: [] for x in self.NTL}
        self.first = {x: set() for x in self.NTL}
        self.follow = {x: set() for x in self.NTL}
        self.second_walk(self.tree)
        if not self.axiom:
            print('ERROR: the grammar axiom was not declared.')
        self.follow[self.axiom] = set('$')
        self.parser_table = {x: {} for x in self.NTL}

    def f_function(self, a):
        if len(a) == 0:
            return set([''])
        elif a[0] in self.TL:
            return set([a[0]])
        elif a[0] in self.NTL:
            if '' not in self.first[a[0]]:
                return self.first[a[0]]
        else:
            try:
                return (self.first[a[0]] - set([''])) | self.f_function(a[1:])
            except IndexError:
                return self.first[a[0]] - set([''])

    def create_first_sets(self):
        added_flag = True
        while added_flag:
            added_flag = False
            for n_term in self.rules:
                for rule in self.rules[n_term]:
                    added_set = self.f_function(rule)
                    sub = added_set - self.first[n_term]
                    self.first[n_term] = self.first[n_term] | added_set
                    if sub:
                        added_flag = True

    def create_follow_sets(self):
        for n_term in self.rules:
            for rule in self.rules[n_term]:
                if len(rule) > 1:
                    for i, elem in enumerate(rule[:-1]):
                        if elem in self.NTL:
                            if rule[i + 1] in self.NTL:
                                self.follow[elem] = self.follow[elem] | (self.first[rule[i + 1]] - set(['']))
                            else:
                                self.follow[elem].add(rule[i + 1])

        added_flag = True
        while added_flag:
            added_flag = False
            for n_term in self.rules:
                for rule in self.rules[n_term]:
                    if len(rule):
                        last = rule[-1]
                        if last in self.NTL:
                            added_set = self.follow[n_term]
                            sub = added_set - self.follow[last]
                            self.follow[last] = self.follow[last] | self.follow[n_term]
                            if sub:
                                added_flag = True

                    if len(rule) > 1:
                        for i, elem in enumerate(rule[:-1]):
                            if elem in self.NTL:
                                if rule[i + 1] in self.NTL and '' in self.first[rule[i + 1]]:
                                    added_set = self.follow[rule[i + 1]]
                                    sub = added_set - self.follow[elem]
                                    self.follow[elem] = self.follow[elem] | self.follow[rule[i + 1]]
                                    if sub:
                                        added_flag = True

    def create_parser_table(self):
        for n_term in self.rules:
            for rule in self.rules[n_term]:
                if len(rule) > 0:
                    if rule[0] in self.NTL:
                        a = self.first[rule[0]]
                    else:
                        a = set([rule[0]])
                    for elem in a:
                        if a != '':
                            try:
                                self.parser_table[n_term][elem]
                                print('ERROR: grammar is not of LL1 class')
                            except KeyError:
                                self.parser_table[n_term][elem] = rule
                    if '' in a:
                        b = self.follow(n_term)
                        for elem in b:
                            try:
                                self.parser_table[n_term][elem]
                                print('ERROR: grammar is not of LL1 class')
                            except KeyError:
                                self.parser_table[n_term][elem] = rule
                if len(rule) == 0:
                    b = self.follow[n_term]
                    for elem in b:
                        try:
                            self.parser_table[n_term][elem]
                            print('ERROR: grammar is not of LL1 class')
                        except KeyError:
                            self.parser_table[n_term][elem] = ['']

    @staticmethod
    def print_tree(tree, f):
        tabs = 0

        def print_node(node, tab_number, f):
           f.write('\t' * tab_number + str(node.marker) + '\n')
           for i in node.children:
               print_node(i, tab_number + 1, f)

        print_node(tree, tabs, f)

    def print_table_to_file(self, f, name):
        f.write(name + ' = ')
        f.write('{')
        for i in self.parser_table:
            f.write('\'' + i + '\': ' + str(self.parser_table[i]) + ',\n')
        f.write('}')
        f.write('\n')
        f.write(name + '_TL = ' + str(self.TL) + '\n')
        f.write(name + '_NTL = ' + str(self.NTL) + '\n')





