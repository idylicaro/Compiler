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
        if : IF LPAREN exp_condition RPAREN if_statement
    '''
    # | command IF LPAREN exp_condition RPAREN.


def p_if_statement(p):
    '''
        if_statement :  LBRACE blockcode RBRACE
            | LBRACE blockcode RBRACE ELSE LBRACE blockcode RBRACE
            | LBRACE blockcode RBRACE elsif
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
    ''' while : WHILE LPAREN exp_condition RPAREN LBRACE blockcode RBRACE
            | WHILE LPAREN exp_condition RPAREN LBRACE RBRACE
    '''


def p_function(p):
    ''' function : SUB ID LPAREN RPAREN LBRACE blockcode RBRACE
        | SUB ID LPAREN function_assignments RPAREN LBRACE blockcode RBRACE
    '''


def p_function_assignments(p):
    ''' function_assignments : exp_assignment
        | exp_assignment COMMA function_assignments
    '''


def p_exp_condition(p):
    # todo: tenta fazer assim exp_condition : exp_condition symbol exp_condition_nextNivel
    '''
    exp_condition : exp_condition GT exp_condition_2
        | exp_condition LT exp_condition_2
        | exp_condition_2
    '''


def p_exp_condition_2(p):
    '''
    exp_condition_2 : exp_condition_2 GE exp_condition_3
        | exp_condition_2 LE exp_condition_3
        | exp_condition_3
    '''


def p_exp_condition_3(p):
    '''
    exp_condition_3 : exp_condition_3 EQ exp_condition_4
        | exp_condition_3 NE exp_condition_4
        | exp_condition_4
    '''


def p_exp_condition_4(p):
    '''
    exp_condition_4 : exp_condition_4 SGT exp_condition_5
        | exp_condition_4 SLT exp_condition_5
        | exp_condition_5
    '''


def p_exp_condition_5(p):
    '''
    exp_condition_5 : exp_condition_5 SGE exp_condition_6
        | exp_condition_5 SLE exp_condition_6
        | exp_condition_6
    '''


def p_exp_condition_6(p):
    '''
    exp_condition_6 : exp_condition_6 SEQ exp_condition_7
        | exp_condition_6 SNE exp_condition_7
        | exp_condition_7
    '''


def p_exp_condition_7(p):
    '''
    exp_condition_7 : exp_condition_7 CMP exp_condition_8
        | exp_condition_8
    '''

def p_exp_condition_8(P):
    '''
    exp_condition_8 : attcond
        | LPAREN exp_condition RPAREN logic exp_condition_logic
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
