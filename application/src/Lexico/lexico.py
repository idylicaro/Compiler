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
    'q': 'Q',
    'qq': 'QQ',
    'qr': 'QR',
    'qw': 'QW',
    'qx': 'QX',
    'no': 'NO',
    's': 'S',
    'sub': 'SUB',
    'tr': 'TR',
    'unless': 'UNLESS',
    'until': 'UNTIL',
    'lt': 'SLT',
    'gt': 'SGT',
    'le': 'SLE',
    'ge': 'SGE',
    'eq': 'SEQ',
    'ne': 'SNE',

}

literals = ['+', '-', '*', '/', '%', '|', '&', '^', '=', '(', ')', '[', ']', '{', '}', ',', '.', ';', ':', '\"', '$']

tokens = [
             'ID', 'NUMBER',
             # Operators (<<, >>, ||, &&, !, <, <=, >, >=, ==, !=)
             'LSHIFT', 'RSHIFT',
             'LOR', 'LAND', 'LNOT',
             'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',

             # Assignment (=, *=, /=, %=, +=, -=, <<=, >>=, &=, ^=, |=)
             'EQUALS', 'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL', 'PLUSEQUAL', 'MINUSEQUAL',
             'LSHIFTEQUAL', 'RSHIFTEQUAL', 'ANDEQUAL', 'XOREQUAL', 'OREQUAL',

             # Increment/decrement (++,--)
             'INCREMENT', 'DECREMENT',

             # Ternary operator (?)
             'TERNARY',

             # Reserved words
             # TODO: move for reserved object
             # 'IT', 'M', 'Y'

         ] + list(reserved.values())

# Operators
t_LSHIFT = r'<<'
t_RSHIFT = r'>>'
t_LOR = r'\|\|'
t_LAND = r'&&'
t_LNOT = r'!'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='

# Assignment operators
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
if (1 + 1) {}
elsif 2 > 3
$x = "Supernaturural"
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
