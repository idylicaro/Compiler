import ply.yacc as yacc
import ply.lex as lex
from .Visitor.VisitorPrettyPrinter import VisitorPrettyPrinter
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
    if p[1] == 'if':
        p[0] = IfStm(p[3], p[5])
    elif p[1] == 'return':
        p[0] = ReturnStm(p[2])
    elif p[1] == 'break':
        p[0] = BreakStm()
    elif p[1] == 'continue':
        p[0] = ContinueStm()
    elif isinstance(p[1], Exp):
        p[0] = p[1]
    else:  # iterations
        p[0] = CommandInterations(p[1])



def p_if_statement(p):
    '''
        if_statement :  LBRACE blockcode RBRACE
            | LBRACE blockcode RBRACE ELSE LBRACE blockcode RBRACE
            | LBRACE blockcode RBRACE elsif
    '''
    if p[4] == 'else':
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
        p[0] = ElsifStm(p[3], p[6])


def p_elsif2(p):
    '''
        elsif2 : elsif
            | ELSE LBRACE blockcode RBRACE
    '''
    if isinstance(p[1], Elsif):
        p[0] = Elsif2Elsif(p[1])
    else:
        p[0] = Elsif2Else(p[1])


def p_interations(p):
    '''
       interations :  FOR LPAREN for_assignments SEMICOLON exp SEMICOLON for_assignments RPAREN LBRACE blockcode RBRACE
       | DO LBRACE blockcode RBRACE WHILE LPAREN exp RPAREN
       | WHILE LPAREN exp RPAREN LBRACE blockcode RBRACE
       | WHILE LPAREN exp RPAREN LBRACE RBRACE
    '''
    if p[1] == 'for':
        p[0] = InterationsFor(p[3], p[5], p[7], p[10])
    elif p[1] == 'do':
        p[0] = InterationsDoWhile(p[3], p[7])
    else:
        if p[6] == '}':
            p[0] = InterationsWhileBlank(p[3])
        else:
            p[0] = InterationsWhile(p[3], p[6])


def p_for_assignments(p):
    ''' for_assignments : exp
        | exp COMMA for_assignments
    '''
    if p[2] == ',':
        p[0] = ForAssignmentsComma(p[1], p[3])
    else:
        p[0] = p[1]


def p_function(p):
    ''' function : SUB ID LPAREN RPAREN LBRACE blockcode RBRACE
        | SUB ID LPAREN function_assignments RPAREN LBRACE blockcode RBRACE
    '''
    if p[4] == ')':
        p[0] = FunctionStmNoParams(p[2], p[6])
    else:
        p[0] = FunctionStm(p[2], p[4], p[7])


def p_function_assignments(p):
    ''' function_assignments : exp
        | exp COMMA function_assignments
    '''
    if p[2] == ',':
        p[0] = FunctionAssignmentsStmComma(p[1], p[3])
    else:
        p[0] = FunctionAssignmentsStm(p[1])


def p_call(p):
    '''
        call : ID LPAREN RPAREN
            | ID LPAREN function_assignments RPAREN
    '''
    if p[3] == ')':
        p[0] = CallStm(p[1], p[3])
    else:
        p[0] = CallStmBlank(p[1])


def p_return(p):
    ''' return : exp '''
    p[0] = ReturnStm(p[1])


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
    if p[1][0] == '$' and p[2] == '=':
        p[0] = ExpAssignmentIdSc(p[1], p[3])
    elif p[1][0] == '@' and p[2] == '=':
        p[0] = ExpAssignmentIdLi(p[1], p[3])
    elif p[2] == '-=':
        p[0] = ExpAssignmentIdScMinus(p[1], p[3])
    elif p[2] == '+=':
        p[0] = ExpAssignmentIdScPlus(p[1], p[3])
    elif p[2] == '%=':
        p[0] = ExpAssignmentIdScMode(p[1], p[3])
    elif p[2] == '/=':
        p[0] = ExpAssignmentIdScDivequal(p[1], p[3])
    elif p[2] == '*=':
        p[0] = ExpAssignmentIdScTimes(p[1], p[3])
    else:
        p[0] = ExpAssignmentLor(p[1])

def p_exp_lor(p):
    '''
        exp_lor : exp_lor LOR exp_land
            | exp_land
    '''
    if p[2] == '||':
        p[0] = ExpLorStm(p[1], p[3])
    else:
        p[0] = ExpLorJustLand(p[1])

def p_exp_land(p):
    '''
        exp_land : exp_land LAND exp_or
            | exp_or
    '''
    if p[2] == '&&':
        p[0] = ExpLandStm(p[1], p[3])
    else:
        p[0] = ExpLandJustOr(p[1])

def p_exp_or(p):
    '''
        exp_or : exp_or OR exp_and
            | exp_and
    '''
    if p[2] == '|':
        p[0] = ExpOrStm(p[1], p[3])
    else:
        p[0] = ExpOrJustAnd(p[1])

def p_exp_and(p):
    '''
        exp_and : exp_and AND exp_comp
            | exp_comp_eq
    '''
    if p[2] == '&':
        p[0] = ExpAndStm(p[1], p[3])
    else:
        p[0] = ExpAndJustCompEq(p[1])

def p_exp_comp_eq(p):
    '''
        exp_comp_eq : exp_comp_eq EQ exp_comp
            | exp_comp_eq NE exp_comp
            | exp_comp_eq SEQ exp_comp
            | exp_comp_eq SNE exp_comp
            | exp_comp_eq CMP exp_comp
            | exp_comp
    '''
    if p[2] == '==':
        p[0] = ExpCompEqEQ(p[1], p[3])
    elif p[2] == '!=':
        p[0] = ExpCompEqNE(p[1], p[3])
    elif p[2] == 'eq':
        p[0] = ExpCompEqSEQ(p[1], p[3])
    elif p[2] == 'ne':
        p[0] = ExpCompEqSNE(p[1], p[3])
    elif p[2] == 'cmp':
        p[0] = ExpCompEqCMP(p[1], p[3])
    else:
        p[0] = ExpCompEqJust(p[1])

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
    if p[2] == '>':
        p[0] = ExpCompGt(p[1], p[3])
    elif p[2] == '<':
        p[0] = ExpCompLt(p[1], p[3])
    elif p[2] == '>=':
        p[0] = ExpCompGe(p[1], p[3])
    elif p[2] == '<=':
        p[0] = ExpCompLe(p[1], p[3])
    elif p[2] == 'lt':
        p[0] = ExpCompSlt(p[1], p[3])
    elif p[2] == 'gt':
        p[0] = ExpCompSgt(p[1], p[3])
    elif p[2] == 'ge':
        p[0] = ExpCompSge(p[1], p[3])
    elif p[2] == 'le':
        p[0] = ExpCompSle(p[1], p[3])
    else:
        p[0] = ExpCompJustPlus(p[1])

def p_exp_plusminus(p):
    '''
        exp_plusminus : exp_plusminus PLUS exp_times_divides
            | exp_plusminus MINUS exp_times_divides
            | exp_times_divides
    '''
    if p[2] == '+':
        p[0] = ExpPlusMinusPlus(p[1], p[3])
    elif p[2] == '-':
        p[0] = ExpPlusMinusMinus(p[1], p[3])
    else:
        p[0] = ExpPlusMinusJustTimes(p[1])

def p_exp_times_divides(p):
    '''
        exp_times_divides : exp_times_divides TIMES exp_lnot
            | exp_times_divides DIVIDE exp_lnot
            | exp_times_divides MODULO exp_lnot
            | exp_lnot
    '''
    if p[2] == '*':
        p[0] = ExpTimesDividesTimes(p[1], p[3])
    elif p[2] == '/':
        p[0] = ExpTimesDividesDivide(p[1], p[3])
    elif p[2] == '%':
        p[0] = ExpTimesDividesModulo(p[1], p[3])
    else:
        p[0] = ExpTimesDividesJustLnot(p[1])

def p_exp_lnot(p):
    '''
    exp_lnot : XOR exp_lnot
        | exp_decrement_increment
    '''
    if p[1] == '^':
        p[0] = ExpLnotXor(p[2])
    else:
        p[0] = ExpLnotJustDecrementIncrement(p[1])

def p_exp_decrement_increment(p):
    '''
    exp_decrement_increment : INCREMENT ID_SC
        | DECREMENT ID_SC
        | ID_SC INCREMENT
        | ID_SC DECREMENT
        | exp_lastlayer
    '''
    if p[1] == '++':
        p[0] = ExpDecrementPreIncrement(p[2])
    elif p[1] == '--':
        p[0] = ExpDecrementPreDecrement(p[2])
    elif p[2] == '++':
        p[0] = ExpDecrementPosIncrement(p[1])
    elif p[2] == '--':
        p[0] = ExpDecrementPosDecrement(p[1])
    else:
        p[0] = ExpDecrementIncrementJustLastLayer(p[1])

def p_exp_lastlayer(p):
    '''
        exp_lastlayer : LPAREN exp RPAREN
        | ID_SC
        | ID_LI
        | NUMBER
        | call
        | TRUE
        | FALSE
    '''

    if isinstance(p[1], int):  # NUMBER
        p[0] = ExpLastlayerIdNumber(p[1])
    else:
        if p[1][0] == '$':  # ID_SC
            p[0] = ExpLastlayerIdSc(p[1])
        elif p[1][0] == '@':  # ID_LI
            p[0] = ExpLastlayerIdLi(p[1])
        elif isinstance(p[1], Call):
            p[0] = ExpLastlayerCall(p[1])
        elif p[1] == '(':
            p[0] = ExpLastlayerExp(p[1])
        elif p[1] == 'true':
            p[0] = ExpLastlayerTrue()
        else:
            p[0] = ExpLastlayerFalse()

parser = yacc.yacc()

while True:
    try:
        more = open('test.txt','r' )
        if more:
            s = lexer.input(more)
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    visitor = VisitorPrettyPrinter()
    result.accept(visitor)
    print(result)
