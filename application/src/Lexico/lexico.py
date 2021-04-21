import ply.lex as lex

tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
    'IDENTIFIER', 'COMMENT',
    '__DATA__', '__END__', '__FILE__', '__LINE__', '__PACKAGE__',
    'AND', 'CMP', 'CONTINUE', 'CORE', 'DO',
    'ELSE', 'ELSIF', 'EQ', 'EXP', 'FOR', 'FOREACH', 'GE', 'GT', 'IF', 'LE',
    'LOCK', 'IT', 'M', 'NE', 'NO', 'OR', 'PACKAGE', 'Q', 'QQ', 'QR',
    'QW', 'QX', 'S', 'SUB', 'TR', 'UNLESS', 'UNTIL', 'WHILE', 'XOR', 'Y'

)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t___DATA__ = '__DATA__'
t___END__ = '__END__'
t___FILE__ = '__FILE__'
t___LINE__ = '__LINE__'
t___PACKAGE__ = '__PACKAGE__'

t_AND = 'and'
t_CMP = 'cmp'
t_CONTINUE = 'continue'
t_CORE = 'CORE'
t_DO = 'do'

t_ELSE = 'else'
t_ELSIF = 'elsif'
t_EQ = 'eq'
t_EXP = 'exp'
t_FOR = 'for'
t_FOREACH = 'foreach'
t_GE = 'ge'
t_GT = 'gt'
t_IF = 'if'
t_LE = 'le'

t_LOCK = 'lock'
t_IT = 'it'
t_M = 'm'
t_NE = 'ne'
t_NO = 'no'
t_OR = 'or'
t_PACKAGE = 'package'
t_Q = 'q'
t_QQ = 'qq'
t_QR = 'qr'

t_QW = 'qw'
t_QX = 'qx'
t_S = 's'
t_SUB = 'sub'
t_UNLESS = 'unless'
t_UNTIL = 'until'
t_WHILE = 'while'
t_XOR = 'xor'
t_Y = 'y'


def t_IDENTIFIER(t):
    r' ([a-zA-Z_])(\w|_)*'
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
_a
abc
eq
cmp
__DATA__ 
'''

# Give the lexer some input
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok.type, tok.value, tok.lineno, tok.lexpos)

# for tok in lexer:
#     print(tok.type, tok.value, tok.lineno, tok.lexpos)
