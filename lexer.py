# lexer.py
# cyrill.sitnikov@gmail.com


class Position(object):
    def __init__(self, program):
        self.program = program
        self.index = 0
        self.sym = 1
        self.line = 1

    def copy_pos(self):
        new_pos = Position(self.program)
        new_pos.index = self.index
        new_pos.sym = self.sym
        new_pos.line = self.line
        return new_pos

    def current_symbol(self):
        if self.index >= len(self.program):
            return None
        else:
            return self.program[self.index]

    def inc(self):
        c = self.current_symbol()
        if c != -1:
            if c == '\n':
                self.line += 1
                self.sym = 1
            else:
                self.sym += 1
            self.index += 1
        return self


class Token(object):
    def __init__(self, domain, image, start, end):
        self.image = image
        self.start = start
        self.end = end
        self.domain = domain

    def __str__(self):
        return '{0} ({1:d}:{2:d})-({3:d}:{4:d}) {5}'.format(str(self.domain), self.start[0], self.start[1],
                                                            self.end[0], self.end[1], self.image)


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
                #print(str(t))
            t = self.next_token()

        return token_list


