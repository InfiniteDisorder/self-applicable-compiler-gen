from LLParserGenerator import *
import sys

pg = LLParserGenerator(open(sys.argv[1]).read())
pg.state_machine.to_file(sys.argv[2])

