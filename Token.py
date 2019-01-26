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
