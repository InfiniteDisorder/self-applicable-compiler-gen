from ParserGenerator import *
import sys

pg = ParserGenerator(open(sys.argv[1]).read())
pg.state_machine.to_file(sys.argv[2])



