from Token import *


class Lexer(object):
    def __init__(self, program):
        self.program = program
        self.pos = Position(self.program)

    def next_token(self):
        start = self.pos.copy_pos()
        while self.pos.current_symbol():
            if self.pos.current_symbol().isspace():
                while self.pos.inc().current_symbol() and self.pos.current_symbol().isspace():
                    pass
                return Token('WS', self.program[start.index: self.pos.index],
                             (start.line, start.sym), (self.pos.line, self.pos.sym))
            elif self.pos.current_symbol() == '<':
                while True:
                    c = self.pos.inc().current_symbol()
                    if c in set(['\n', '\t', '\r']) or c == -1:
                        return Token('E', self.program[start.index: self.pos.index],
                                    (start.line, start.sym), (self.pos.line, self.pos.sym))
                    if c == '>':
                        self.pos.inc()
                        return Token('I', self.program[start.index: self.pos.index],
                        (start.line, start.sym), (self.pos.line, self.pos.sym))
            elif self.pos.current_symbol().isalpha():
                while self.pos.current_symbol() and self.pos.inc().current_symbol().isalpha():
                    pass
                image = self.program[start.index: self.pos.index]
                if image == 'tokens':
                    return Token('T', 'tokens',
                    (start.line, start.sym), (self.pos.line, self.pos.sym))
                elif image == 'start':
                    return Token('ST', 'start',
                    (start.line, start.sym), (self.pos.line, self.pos.sym))
                elif image == 'is':
                    return Token('IS', 'is',
                    (start.line, start.sym), (self.pos.line, self.pos.sym))
                else:
                    return Token('E', self.program[start.index: self.pos.index],
                    (start.line, start.sym), (self.pos.line, self.pos.sym))
            elif self.pos.current_symbol() == ',':
                self.pos.inc()
                return Token('comma', ',',
                (start.line, start.sym), (self.pos.line, self.pos.sym))
            elif self.pos.current_symbol() == '.':
                self.pos.inc()
                return Token('dot', '.',
                (start.line, start.sym), (self.pos.line, self.pos.sym))

            else:
                self.pos.inc()
                return Token('E', self.program[start.index: self.pos.index],
                    (start.line, start.sym), (self.pos.line, self.pos.sym))
        return Token('EOF', self.program[start.index: self.pos.index],
            (start.line, start.sym), (self.pos.line, self.pos.sym))

    def analyze(self):
        t = self.next_token()
        token_list = []
        while t.domain != 'EOF':
            if t.domain != 'WS':
                token_list.append(t)
            t = self.next_token()

        return token_list


