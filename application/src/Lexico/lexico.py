import ply.lex as lex

reserved = {
    # Value : token
    '__DATA__': '__DATA__',
    '__END__': '__END__',
    '__FILE__': '__FILE__',
    '__LINE__': '__LINE__',
    '__PACKAGE__': '__PACKAGE__',
    'if': 'IF',
    'else': 'ELSE',
    'elsif': 'ELSIF',
    'for': 'FOR',
    'foreach': 'FOREACH',
    'while': 'WHILE',
    'continue': 'CONTINUE',
    'CORE': 'CORE',
    'do': 'DO',
    'exp': 'EXP',
    'cmp': 'CMP',
    'package': 'PACKAGE',

}
tokens = [
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
             # TODO: move for reserverd object
             'LOCK', 'IT', 'M', 'NO', 'Q', 'QQ', 'QR',
             'QW', 'QX', 'S', 'SUB', 'TR', 'UNLESS', 'UNTIL', 'Y'

         ] + list(reserved.values())

# Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_OR = r'\|'
t_AND = r'&'
t_XOR = r'\^'
t_LSHIFT = r'<<'
t_RSHIFT = r'>>'
t_LOR = r'\|\|'
t_LAND = r'&&'
t_LNOT = r'!'
t_LT = r'<'  # TODO: tem outra forma que no caso é para string que é : lt
t_GT = r'>'  # TODO: tem outra forma que no caso é para string que é : gt
t_LE = r'<='  # TODO: tem outra forma que no caso é para string que é : le
t_GE = r'>='  # TODO: tem outra forma que no caso é para string que é : ge
t_EQ = r'=='  # TODO: tem outra forma que no caso é para string que é : eq
t_NE = r'!='  # TODO: tem outra forma que no caso é para string que é : ne

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

# TODO: precisa ver essa questão de palavras reservadas, pq deixando fazendo desta forma ta sendo ignorado e ta indo tudo como ID
t_LOCK = 'lock'
t_IT = 'it'
t_M = 'm'
t_NO = 'no'
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


# Identifiers
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
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
if
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
