from arithmetic_table import table as t
from arithmetic_table import productions as p

from LALRTreeBuilder import *
from ArithmeticLexer import ArithmeticLexer as Lexer
from ArithmeticTreeTraverse import traverse

build = LALRTreeBuilder(t, p).builder()
tree = build(Lexer('1 + 2 * 3 * (3 * 3 - 2 * (9 - 0)) ').analyze())

while True:
    expression = input('Enter arithmetic expression:\n')
    if expression:
        build = LALRTreeBuilder(t, p).builder()
        tree = build(Lexer(expression).analyze())
        print(traverse(tree))
    else:
        break


