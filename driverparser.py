import sys
from ply import * 
import c_parser
from util import build_tree

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

print(build_tree(commands))
