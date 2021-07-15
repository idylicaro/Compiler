import ply.yacc as yacc
import ply.lex as lex
from src.Lexicon.lexico import tokens

def p_init(p):
    '''init : blockcode init
        | function init
        | blockcode
        | function
        '''

def p_blockcode(P):
    ''' blockcode : command
        | command blockcode
    '''

def p_command(p):
    ''' command : interations
        | if
        | exp_assignment
        | call
        | RETURN return SEMICOLON
        | BREAK SEMICOLON
        | CONTINUE SEMICOLON
    '''

def p_interations(p):
    '''
       interations :  for
       | dowhile
       | while
    '''

def p_for(p):
    ''' for : FOR LPAREN for_assignments SEMICOLON condition SEMICOLON for_assignments RPAREN LBRACE blockcode RBRACE'''

def p_for_assignments(p):
    ''' for_assignments : exp_assignment
        | exp_assignment COMMA for_assignments
    '''

def p_dowhile(p):
    ''' dowhile :  DO LBRACE blockcode RBRACE WHILE LPAREN condition RPAREN '''

def p_while(p):
    ''' while :  LPAREN condition RPAREN LBRACE blockcode RBRACE '''

def p_function(p):
    ''' function : SUB IDENTIFIER LPAREN RPAREN LBRACE blockcode RBRACE
        | SUB IDENTIFIER LPAREN function_assignments RPAREN LBRACE blockcode RBRACE
    '''

def p_function_assignments(p):
    ''' function_assignments : exp_assignment
        | exp_assignment COMMA function_assignments
    '''

def p_condition(p):
    # | ((CONDITION) [LOGIC (CONDITION)]*)
    '''
    condition : attcond GT attcond
            | attcond LT attcond
            | attcond EQ attcond
            | attcond GE attcond
            | attcond LE attcond
            | attcond NE attcond
            | attcond
            | attcond CMP attcond
            | attcond SEQ attcond
            | attcond SNE attcond
            | attcond SLT attcond
            | attcond SGT attcond
            | attcond SLE attcond
            | attcond SGE attcond
    '''

def p_exp_assignment(p):
    ''' exp_assignment : IDENTIFIER_SC EQUALS arithmetic
        | IDENTIFIER_LI EQUALS arithmetic
        | IDENTIFIER_SC
        | IDENTIFIER_LI
        | INCREMENT IDENTIFIER_SC
        | DECREMENT IDENTIFIER_SC
        | IDENTIFIER_SC INCREMENT
        | IDENTIFIER_SC DECREMENT
    '''

def p_arithmetic(p):
    '''
        arithmetic : exp
    '''

def p_exp(p):
    '''
        exp : exp PLUS exp1
            | exp MINUS exp1
            | exp1
    '''

def p_exp1(p):
    '''
        exp1 : exp1 TIMES exp2
            | exp1 DIVIDE exp2
            | exp1 MODULO exp2
            | exp2
    '''

def p_exp2(p):
    '''
    exp2 : exp3 XOR exp2
        | exp3
    '''

def p_exp3(p):
    '''
    exp3 : LPAREN arithmetic RPAREN
        | NUMBER
        | exp_assignment
        | call
        | exp
    '''

def p_attcond(p):
    ''' attcond : exp_assignment
        | NUMBER
        | true
        | false
    '''

def p_call(p):
    '''
        call : IDENTIFIER LPAREN RPAREN
            | IDENTIFIER LPAREN function_assignments RPAREN
    '''

parser = yacc.yacc()

while True:
 try:
     s = input('perl > ')
 except EOFError:
     break
 if not s: continue
 result = parser.parse(s)
 print(result)
