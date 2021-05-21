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



def build_tree(root):
    return '\n'.join(_build_tree(root))


def _build_tree(node):
    if not isinstance(node, tuple):
        yield str(node)
        return

    values = [_build_tree(n) for n in node]
    if len(values) == 1:
        yield from build_lines('──', '  ', values[0])
        return

    start, *mid, end = values
    yield from build_lines('┬─', '│ ', start)
    for value in mid:
        yield from build_lines('├─', '│ ', value)
    yield from build_lines('└─', '  ', end)


def build_lines(first, other, values):
    yield first + next(values)
    for value in values:
        yield other + value


print(build_tree(commands))
#for i in range(len(commands)):
   # print(commands[i])
