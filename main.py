import sys
from c_parser import *
from code_generation import parse


if __name__ == "__main__":

    text = open(sys.argv[1], "r")

    try:
        ast = yacc.parse(text.read())
        semantic_declation_check()
    except ParseException as e:
        print(e)
    else:
        ast_file = open('ast', 'w')
        ast_file.write(str(ast))

        asm = open(sys.argv[2], 'w+')
        asm.write('# Generated from: ' + sys.argv[1] + '\n')

        parse(ast, asm)

