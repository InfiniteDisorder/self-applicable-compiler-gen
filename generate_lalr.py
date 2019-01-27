from LALRParserGenerator import *
import sys

pg = LALRParserGenerator(open(sys.argv[1]).read())
# pg.state_machine.to_file(sys.argv[2])

