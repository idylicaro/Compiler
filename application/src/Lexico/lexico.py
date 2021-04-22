import ply.lex as lex

tokens = (
    'ID', 'NUMBER',
    # Operators (+, -, *, /, %, |, &, ^, <<, >>, ||, &&, !, <, <=, >, >=, ==, !=)
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO',
    'OR', 'AND', 'XOR', 'LSHIFT', 'RSHIFT',
    'LOR', 'LAND', 'LNOT',
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',

    # Assignment (=, *=, /=, %=, +=, -=, <<=, >>=, &=, ^=, |=)
    'EQUALS', 'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL', 'PLUSEQUAL', 'MINUSEQUAL',
    'LSHIFTEQUAL', 'RSHIFTEQUAL', 'ANDEQUAL', 'XOREQUAL', 'OREQUAL',

    # Increment/decrement (++,--)
    'INCREMENT', 'DECREMENT',

    # Ternary operator (?)
    'TERNARY',

    # Delimeters ( ) [ ] { } , . ; :
    'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE',
    'COMMA', 'PERIOD', 'SEMI', 'COLON',

    # Reserved words
    '__DATA__', '__END__', '__FILE__', '__LINE__', '__PACKAGE__',
    'CMP', 'CONTINUE', 'CORE', 'DO',
    'ELSE', 'ELSIF', 'EXP', 'FOR', 'FOREACH', 'IF',
    'LOCK', 'IT', 'M', 'NO', 'PACKAGE', 'Q', 'QQ', 'QR',
    'QW', 'QX', 'S', 'SUB', 'TR', 'UNLESS', 'UNTIL', 'WHILE', 'Y'

)

# Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_OR = r'\|'
t_AND = r'&'
t_NOT = r'~'
t_XOR = r'\^'
t_LSHIFT = r'<<'
t_RSHIFT = r'>>'
t_LOR = r'\|\|'
t_LAND = r'&&'
t_LNOT = r'!'
t_LT = r'<'  #TODO: tem outra forma que no caso é para string que é : lt
t_GT = r'>'  #TODO: tem outra forma que no caso é para string que é : gt
t_LE = r'<=' #TODO: tem outra forma que no caso é para string que é : le
t_GE = r'>=' #TODO: tem outra forma que no caso é para string que é : ge
t_EQ = r'==' #TODO: tem outra forma que no caso é para string que é : eq
t_NE = r'!=' #TODO: tem outra forma que no caso é para string que é : ne

# Assignment operators
t_EQUALS = r'='
t_TIMESEQUAL = r'\*='
t_DIVEQUAL = r'/='
t_MODEQUAL = r'%='
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='
t_LSHIFTEQUAL = r'<<='
t_RSHIFTEQUAL = r'>>='
t_ANDEQUAL = r'&='
t_OREQUAL = r'\|='
t_XOREQUAL = r'\^='

t___DATA__ = '__DATA__'
t___END__ = '__END__'
t___FILE__ = '__FILE__'
t___LINE__ = '__LINE__'
t___PACKAGE__ = '__PACKAGE__'

t_CMP = 'cmp'
t_CONTINUE = 'continue'
t_CORE = 'CORE'
t_DO = 'do'

t_ELSE = 'else'
t_ELSIF = 'elsif'
t_EXP = 'exp'
t_FOR = 'for'
t_FOREACH = 'foreach'
t_IF = 'if'

t_LOCK = 'lock'
t_IT = 'it'
t_M = 'm'
t_NO = 'no'
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
t_Y = 'y'


def t_ID(t):
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
