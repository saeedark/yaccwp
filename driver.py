import sys
from ply import * 
import lexer


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

        printstr("\nHello,")  /* forgot ;*/
        printstr(" World!");

        return;
    }
    """

# Build the lexer
#lexer = lex.lex()

# Give the lexer some input
lex.input(data)

# Tokenize
while True:
    tok = lex.token()
    if not tok:
        break      # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
