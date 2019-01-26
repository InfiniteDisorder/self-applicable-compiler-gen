from arithm_table import *
from ArithmeticLexer import *
from LLTreeBuilder import *

while True:
    expression = input('Enter arithmetic expression:\n')
    if expression:
        tokens = ArithmeticLexer(expression).analyze()
        tree = build_tree(tokens, arithmetic_TL, arithmetic_NTL, arithmetic, 'E')
        print(process_arithmetic_tree(tree))
    else:
        break


