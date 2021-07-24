import ply.yacc as yacc
import ply.lex as lex
from src.Lexicon.lexico import tokens
from .abstractSyntax.index import *


def p_init(p):
    '''init : command init
        | command
        | function init
        | function
    '''
    if isinstance(p[1], Command):
        if p[2] is not None:
            InitCommandInit(p[1], p[2])
        else:
            InitCommand(p[1])
    if isinstance(p[1], Function):
        if p[2] is not None:
            InitFunctionInit(p[1], p[2])
        else:
            InitFunction(p[1])


def p_blockcode(p):
    ''' blockcode : command
        | blockcode command
    '''
    if p[2] is not None:
        BlockcodeBcdCommand(p[1], p[2])
    else:
        BlockcodeCommand(p[1])


def p_command(p):
    ''' command : interations
        | IF LPAREN exp RPAREN if_statement
        | exp SEMICOLON
        | RETURN return SEMICOLON
        | BREAK SEMICOLON
        | CONTINUE SEMICOLON
    '''
    if p[1] == tokens.IF:
        p[0] = IfStm(p[3], p[5])
    elif p[1] == tokens.RETURN:
        p[0] = ReturnStm(p[2])
    elif p[1] == tokens.BREAK:
        pass
    elif p[1] == tokens.CONTINUE:
        pass
    elif isinstance(p[1], Exp):
        p[0] = ExpAssignmentIdSc(p[1])
    else:  # iterations
        p[0] = CommandInterations(p[1])
        # how do make it?


def p_if_statement(p):
    '''
        if_statement :  LBRACE blockcode RBRACE
            | LBRACE blockcode RBRACE ELSE LBRACE blockcode RBRACE
            | LBRACE blockcode RBRACE elsif
    '''
    if p[4] == tokens.ELSE:
        p[0] = IfStatementBlockcodeElse(p[2], p[6])
    elif isinstance(p[4], Elsif):
        p[0] = IfStatementBlockcodeElsif(p[2], p[4])
    else:
        p[0] = IfStatementBlockcode(p[2])

def p_elsif(p):
    '''
        elsif : ELSIF LPAREN exp RPAREN LBRACE blockcode RBRACE
        | ELSIF LPAREN exp RPAREN LBRACE blockcode RBRACE elsif2
    '''
    if isinstance(p[8], Elsif2):
        p[0] = ElsifStmElsif2(p[3], p[6], p[8])
    else:
        p[0] = ElsifStm(p[3],p[6])

def p_elsif2(p):
    '''
        elsif2 : elsif
            | ELSE LBRACE blockcode RBRACE
    '''
    if isinstance(p[1], Elsif):
        p[0] = Elsif2Elsif(p[1])
    else :
        p[0] = Elsif2Else(p[1])


def p_interations(p):
    '''
       interations :  FOR LPAREN for_assignments SEMICOLON exp SEMICOLON for_assignments RPAREN LBRACE blockcode RBRACE
       | DO LBRACE blockcode RBRACE WHILE LPAREN exp RPAREN
       | WHILE LPAREN exp RPAREN LBRACE blockcode RBRACE
       | WHILE LPAREN exp RPAREN LBRACE RBRACE
    '''


def p_for_assignments(p):
    ''' for_assignments : exp
        | exp COMMA for_assignments
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
    exp_decrement_increment : INCREMENT ID_SC
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
