import ply.yacc as yacc
import ply.lex as lex
from src.Lexicon.lexico import tokens


def p_init(p):
    '''init : command init
        | command
        | function init
        | function
        '''


def p_blockcode(P):
    ''' blockcode : command
        | blockcode command
    '''


def p_command(p):
    ''' command : interations
        | if
        | exp SEMICOLON
        | RETURN return SEMICOLON
        | BREAK SEMICOLON
        | CONTINUE SEMICOLON
    '''


def p_if(p):
    '''
        if : IF LPAREN exp RPAREN if_statement
    '''
    # | command IF LPAREN exp RPAREN.


def p_if_statement(p):
    '''
        if_statement :  LBRACE blockcode RBRACE
            | LBRACE blockcode RBRACE ELSE LBRACE blockcode RBRACE
            | LBRACE blockcode RBRACE elsif
    '''


def p_elsif(p):
    '''
        elsif : ELSIF LPAREN exp RPAREN LBRACE blockcode RBRACE
        | ELSIF LPAREN exp RPAREN LBRACE blockcode RBRACE elsif2
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
    ''' for : FOR LPAREN for_assignments SEMICOLON exp SEMICOLON for_assignments RPAREN LBRACE blockcode RBRACE'''


def p_for_assignments(p):
    ''' for_assignments : exp
        | exp COMMA for_assignments
    '''


def p_dowhile(p):
    ''' dowhile :  DO LBRACE blockcode RBRACE WHILE LPAREN exp RPAREN '''


def p_while(p):
    ''' while : WHILE LPAREN exp RPAREN LBRACE blockcode RBRACE
            | WHILE LPAREN exp RPAREN LBRACE RBRACE
    '''


def p_function(p):
    ''' function : SUB ID LPAREN RPAREN LBRACE blockcode RBRACE
        | SUB ID LPAREN function_assignments RPAREN LBRACE blockcode RBRACE
    '''


def p_function_assignments(p):
    ''' function_assignments : exp
        | exp COMMA function_assignments
    '''


def p_call(p):
    '''
        call : ID LPAREN RPAREN
            | ID LPAREN function_assignments RPAREN
    '''


def p_return(p):
    ''' return : exp '''


def p_exp(p):
    ''' exp : ID_SC EQUALS exp_lor
        | ID_LI EQUALS exp_lor
        | ID_SC MINUSEQUAL exp_lor
        | ID_SC PLUSEQUAL exp_lor
        | ID_SC MODEQUAL exp_lor
        | ID_SC DIVEQUAL exp_lor
        | ID_SC TIMESEQUAL exp_lor
        | exp_lor
    '''


def p_exp_lor(p):
    '''
        exp_lor : exp_lor LOR exp_land
            | exp_land
    '''

def p_exp_land(p):
    '''
        exp_land : exp_land LAND exp_or
            | exp_or
    '''

def p_exp_or(p):
    '''
        exp_or : exp_or OR exp_and
            | exp_and
    '''

def p_exp_and(p):
    '''
        exp_and : exp_and AND exp_comp
            | exp_comp_eq
    '''

def p_exp_comp_eq(p):
    '''
        exp_comp_eq : exp_comp_eq EQ exp_comp
            | exp_comp_eq NE exp_comp
            | exp_comp_eq SEQ exp_comp
            | exp_comp_eq SNE exp_comp
            | exp_comp_eq CMP exp_comp
            | exp_comp
    '''

def p_exp_comp(p):
    '''
        exp_comp : exp_comp GT exp_plusminus
            | exp_comp LT exp_plusminus
            | exp_comp GE exp_plusminus
            | exp_comp LE exp_plusminus
            | exp_comp SLT exp_plusminus
            | exp_comp SGT exp_plusminus
            | exp_comp SGE exp_plusminus
            | exp_comp SLE exp_plusminus
            | exp_plusminus
    '''


def p_exp_plusminus(p):
    '''
        exp_plusminus : exp_plusminus PLUS exp_times_divides
            | exp_plusminus MINUS exp_times_divides
            | exp_times_divides
    '''


def p_exp_times_divides(p):
    '''
        exp_times_divides : exp_times_divides TIMES exp_lnot
            | exp_times_divides DIVIDE exp_lnot
            | exp_times_divides MODULO exp_lnot
            | exp_lnot
    '''


def p_exp_lnot(p):
    '''
    exp_lnot : XOR exp_lnot
        | exp_decrement_increment
    '''


def p_exp_decrement_increment(p):
    '''
    exp_decrement_increment : INCREMENT  ID_SC
        | DECREMENT ID_SC
        | ID_SC INCREMENT
        | ID_SC DECREMENT
        | exp_lastlayer
    '''

def p_exo_lastlayer(p):
    '''
        exp_lastlayer : LPAREN exp RPAREN
        | ID_SC
        | ID_LI
        | NUMBER
        | call
        | TRUE
        | FALSE
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
