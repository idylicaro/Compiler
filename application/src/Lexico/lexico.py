import ply.lex as lex

tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'IF',
    'ELSE',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
