import ply.lex as lex

reserved = {
    # Value : token
    '__DATA__': '__DATA__',
    '__END__': '__END__',
    '__FILE__': '__FILE__',
    '__LINE__': '__LINE__',
    '__PACKAGE__': '__PACKAGE__',
    'else': 'ELSE',
    'elsif': 'ELSIF',
    'for': 'FOR',
    'foreach': 'FOREACH',
    'while': 'WHILE',
    # 'continue': 'CONTINUE',
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

tokens = [
             'ID_SC', 'ID_LI', 'ID', 'NUMBER', 'RETURN', 'CONTINUE',
             'IF',
             # Operators (+, -, *, /, %, |, &, ^, <<, >>, ||, &&, !, <, <=, >, >=, ==, !=)
             'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO',
             'OR', 'AND', 'XOR',
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

             # Delimeters ( ) [ ] { } , . ; :
             'LPAREN', 'RPAREN',
             'LBRACKET', 'RBRACKET',
             'LBRACE', 'RBRACE',
             'COMMA', 'PERIOD', 'SEMICOLON', 'COLON',

             # Reserved words
             # TODO: move for reserved object
             # 'IT', 'M', 'Y'

         ] + list(reserved.values())

def t_RETURN(t): r'return'; return t
t_CONTINUE = r'continue'


def t_IF(t): r'if'; return t


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
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='

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

# Delimeters
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_PERIOD = r'.'
t_SEMICOLON = r';'
t_COLON = r':'


# Identifiers
def t_ID_SC(t):
    r'\$[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID_SC')  # Check for reserved words
    return t


def t_ID_LI(t):
    r'@[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID_LI')  # Check for reserved words
    return t


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
$_a
@_b
ab
if(){}
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
