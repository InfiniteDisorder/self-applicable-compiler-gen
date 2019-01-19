# main.py
# cyrill.sitnikov@gmail.com
# parser generator, variant 5

from parser_generator import *
import sys

g = ParserGenerator(open(sys.argv[1]).read())
g.print_table_to_file(open(sys.argv[2], 'w'), 'arithmetic')

f = ParserGenerator(open(sys.argv[3]).read())
f.print_table_to_file(open(sys.argv[4], 'w'), 'self_table')




