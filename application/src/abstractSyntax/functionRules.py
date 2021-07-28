from .abstractClasses import Function, FunctionAssignments


class FunctionStmNoParams(Function):
    def __init__(self, id, blockcode):
        self.id = id
        self.stm = blockcode

    def accept(self, visitor):
        visitor.visitFunctionStmNoParams(self)


class FunctionStm(Function):
    def __init__(self, id, function_assignments, blockcode):
        self.id = id
        self.stm = function_assignments
        self.stm2 = blockcode

    def accept(self, visitor):
        visitor.visitFunctionStm(self)

class FunctionAssignmentsStm(FunctionAssignments):
    def __init__(self, exp):
        self.stm = exp

    def accept(self, visitor):
        visitor.visitFunctionAssignmentsStm(self)

class FunctionAssignmentsStmComma(FunctionAssignments):
    def __init__(self, exp, function_assignments):
        self.stm = exp
        self.stm2 = function_assignments

    def accept(self, visitor):
        visitor.visitFunctionAssignmentsStmComma(self)