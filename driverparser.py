import sys
from ply import * 
import parser

if len(sys.argv) > 1:
    data = open(sys.argv[1], 'rb').read().decode('utf-8')
else:
    data = \
    """
    void main()
    {
        int k = 10;
        int i;
        for(i = 0; i < 10; i++)
        {
            if (i >= 5)
            {
                k += i;
            }
        }

        printstr(" World!");

        return;
    }
    """
commands = yacc.parse(data)


def tupleprint(s, x):
    if isinstance(s, tuple):
        for i in range(len(s)):
            tupleprint(s[i], x+3)
    else:
        print("  "*x + str(s))

tupleprint(commands, 0)

#for i in range(len(commands)):
   # print(commands[i])
