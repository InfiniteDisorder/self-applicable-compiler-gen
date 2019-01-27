# main.py
# cyrill.sitnikov@gmail.com
# parser generator, variant 5

from ParserGenerator import *
import sys

pg = ParserGenerator(open(sys.argv[1]).read())
pg.state_machine.to_file(sys.argv[2])

from arithm_table import table as t
from arithm_table import productions as p

from LALRTreeBuilder import *
from ArithmeticLexer import ArithmeticLexer as Lexer

build = LALRTreeBuilder(t, p).builder()
tree = build(Lexer('1 + 2 * 3 * (3 * 3 - 2 * (9 - 0)) ').analyze())

pass
#.print_table_to_file(open(sys.argv[2], 'w'), 'arithmetic')

# f = ParserGenerator(open(sys.argv[3]).read())
# f.print_table_to_file(open(sys.argv[4], 'w'), 'self_table')




