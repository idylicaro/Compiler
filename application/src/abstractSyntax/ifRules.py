from .abstractClasses import If, IfStatement, Elsif, Elsif2


class IfStm(If):
    def __init__(self, exp, ifStm):
        self.stm = exp
        self.stm2 = ifStm

    def accept(self, visitor):
        visitor.visitIfStm(self)


class IfStatementBlockcode(IfStatement):
    def __init__(self, blockcode):
        self.stm = blockcode

    def accept(self, visitor):
        visitor.visitIfStatementBlockcode(self)


class IfStatementBlockcodeElse(IfStatement):
    def __init__(self, blockcode, blockcode2):
        self.stm = blockcode
        self.stm2 = blockcode2

    def accept(self, visitor):
        visitor.visitIfStatementBlockcodeElse(self)


class IfStatementBlockcodeElsif(IfStatement):
    def __init__(self, blockcode, elsif):
        self.stm = blockcode
        self.stm2 = elsif

    def accept(self, visitor):
        visitor.visitIfStatementBlockcodeElsif(self)


class ElsifStm(Elsif):
    def __init__(self, exp, blockcode):
        self.stm = exp
        self.stm2 = blockcode

    def accept(self, visitor):
        visitor.visitElsifStm(self)


class ElsifStmElsif2(Elsif):
    def __init__(self, exp, blockcode, elsif):
        self.stm = exp
        self.stm2 = blockcode
        self.stm3 = elsif

    def accept(self, visitor):
        visitor.visitElsifStmElsif2(self)


class Elsif2Elsif(Elsif2):
    def __init__(self, elsif):
        self.stm = elsif

    def accept(self, visitor):
        visitor.visitElsif2Elsif(self)


class Elsif2Else(Elsif2):
    def __init__(self, blockcode):
        self.stm = blockcode

    def accept(self, visitor):
        visitor.visitElsif2Else(self)
