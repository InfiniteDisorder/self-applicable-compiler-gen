from LLTreeBuilder import *

class ArithmeticLexer(object):
    def __init__(self, program):
        self.program = program
        self.pos = Position(self.program)

    def next_token(self):
        start = self.pos.copy_pos()
        while self.pos.current_symbol():
            if self.pos.current_symbol().isspace():
                while self.pos.inc().current_symbol() and self.pos.current_symbol().isspace():
                    pass
                return Token('space', self.program[start.index: self.pos.index],
                             (start.line, start.sym), (self.pos.line, self.pos.sym))
            elif self.pos.current_symbol().isdigit():
                while self.pos.inc().current_symbol() and self.pos.current_symbol().isdigit():
                    pass
                image = self.program[start.index: self.pos.index]
                return Token('n', self.program[start.index: self.pos.index],
                             (start.line, start.sym), (self.pos.line, self.pos.sym))
            elif self.pos.current_symbol() == '+':
                self.pos.inc()
                return Token('plus', '+',
                             (start.line, start.sym), (self.pos.line, self.pos.sym))
            elif self.pos.current_symbol() == '-':
                self.pos.inc()
                return Token('minus', '-',
                             (start.line, start.sym), (self.pos.line, self.pos.sym))
            elif self.pos.current_symbol() == '/':
                self.pos.inc()
                return Token('div', '/',
                             (start.line, start.sym), (self.pos.line, self.pos.sym))
            elif self.pos.current_symbol() == '*':
                self.pos.inc()
                return Token('mul', '*',
                             (start.line, start.sym), (self.pos.line, self.pos.sym))
            elif self.pos.current_symbol() == '(':
                self.pos.inc()
                return Token('lparen', '(',
                             (start.line, start.sym), (self.pos.line, self.pos.sym))
            elif self.pos.current_symbol() == ')':
                self.pos.inc()
                return Token('rparen', ')',
                             (start.line, start.sym), (self.pos.line, self.pos.sym))
            else:
                self.pos.inc()
                return Token('error', self.program[start.index: self.pos.index],
                             (start.line, start.sym), (self.pos.line, self.pos.sym))
        return Token('eof', self.program[start.index: self.pos.index],
                     (start.line, start.sym), (self.pos.line, self.pos.sym))

    def analyze(self):
        t = self.next_token()
        token_list = []
        while t.domain != 'eof':
            if t.domain != 'space':
                token_list.append(t)
            t = self.next_token()

        return token_list


def F(node):
    if node.children[0].marker.domain == 'left_paren':
        return E(node.children[1])
    if node.children[0].marker.domain == 'n':
        return float(node.children[0].marker.image)

def E(node):
    return T(node.children[0]) + E1(node.children[1])

def E1(node):
    if node.children:
        return T(node.children[1]) + E1(node.children[2])
    else:
        return 0

def T(node):
    return F(node.children[0]) * T1(node.children[1])

def T1(node):
    if node.children:
        return F(node.children[1]) * T1(node.children[2])
    else:
        return 1

def process_arithmetic_tree(tree):
    return E(tree)
