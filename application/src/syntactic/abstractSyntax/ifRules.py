from .abstractClasses import If, IfStatement, Elsif, Elsif2


class IfStm(If):
    def __init__(self, exp, ifStm):
        self.stm = exp
        self.stm2 = ifStm


class IfStatementBlockcode(IfStatement):
    def __init__(self, blockcode):
        self.stm = blockcode


class IfStatementBlockcodeElse(IfStatement):
    def __init__(self, blockcode, blockcode2):
        self.stm = blockcode
        self.stm2 = blockcode2


class IfStatementBlockcodeElsif(IfStatement):
    def __init__(self, blockcode, elsif):
        self.stm = blockcode
        self.stm2 = elsif


class ElsifStm(Elsif):
    def __init__(self, exp, blockcode):
        self.stm = exp
        self.stm2 = blockcode


class ElsifStmElsif2(Elsif):
    def __init__(self, exp, blockcode, elsif):
        self.stm = exp
        self.stm2 = blockcode
        self.stm3 = elsif


class Elsif2Elsif(Elsif2):
    def __init__(self, elsif):
        self.stm = elsif


class Elsif2Else(Elsif2):
    def __init__(self, blockcode):
        self.stm = blockcode
