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

def p_if(p):
    '''
        if : IF LPAREN exp_condition RPAREN LBRACE blockcode RBRACE
        | command IF LPAREN exp_condition RPAREN
        | IF LPAREN exp_condition RPAREN LBRACE blockcode RBRACE ELSE LBRACE blockcode RBRACE
        | IF LPAREN exp_condition RPAREN LBRACE blockcode RBRACE elsif
    '''
def p_elsif(p):
    '''
        elsif : ELSIF LPAREN exp_condition RPAREN LBRACE blockcode RBRACE
        | ELSIF LPAREN exp_condition RPAREN LBRACE blockcode RBRACE elsif2
    '''
def p_elsif2(p):
    '''
        elsif2 : elsif
            | ELSE LBRACE blockcode RBRACE
    '''

def p_interations(p):
    '''
       interations :  for
       | dowhile
       | while
    '''

def p_for(p):
    ''' for : FOR LPAREN for_assignments SEMICOLON exp_condition SEMICOLON for_assignments RPAREN LBRACE blockcode RBRACE'''

def p_for_assignments(p):
    ''' for_assignments : exp_assignment
        | exp_assignment COMMA for_assignments
    '''

def p_dowhile(p):
    ''' dowhile :  DO LBRACE blockcode RBRACE WHILE LPAREN exp_condition RPAREN '''

def p_while(p):
    ''' while :  LPAREN exp_condition RPAREN LBRACE blockcode RBRACE '''

def p_function(p):
    ''' function : SUB ID LPAREN RPAREN LBRACE blockcode RBRACE
        | SUB ID LPAREN function_assignments RPAREN LBRACE blockcode RBRACE
    '''

def p_function_assignments(p):
    ''' function_assignments : exp_assignment
        | exp_assignment COMMA function_assignments
    '''

def p_exp_condition(p):
    # | ((exp_condition) [LOGIC (exp_condition)]*)
    '''
    exp_condition : attcond GT attcond
            | attcond LT attcond
            | attcond EQ attcond
            | attcond GE attcond
            | attcond LE attcond
            | attcond NE attcond
            | attcond
            | LPAREN exp_condition RPAREN logic exp_condition_logic
            | attcond CMP attcond
            | attcond SEQ attcond
            | attcond SNE attcond
            | attcond SLT attcond
            | attcond SGT attcond
            | attcond SLE attcond
            | attcond SGE attcond
    '''
def p_exp_condition_logic(p):
    '''
        exp_condition_logic : LPAREN exp_condition RPAREN
        | LPAREN exp_condition RPAREN logic LPAREN exp_condition RPAREN
    '''

def p_logic(p):
    '''
        logic : LAND
            | LOR
            | LNOT
    '''

def p_exp_assignment(p):
    ''' exp_assignment : ID_SC EQUALS arithmetic
        | ID_LI EQUALS arithmetic
        | ID_SC
        | ID_LI
        | INCREMENT ID_SC
        | DECREMENT ID_SC
        | ID_SC INCREMENT
        | ID_SC DECREMENT
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
        | exp_condition
        | call
        | exp
        | TRUE
        | FALSE
    '''

def p_attcond(p):
    ''' attcond : exp_assignment
        | NUMBER
        | TRUE
        | FALSE
    '''

def p_call(p):
    '''
        call : ID LPAREN RPAREN
            | ID LPAREN function_assignments RPAREN
    '''

def p_return(p):
    ''' return : attcond
        | arithmetic
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
