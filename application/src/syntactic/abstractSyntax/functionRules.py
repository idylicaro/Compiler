from abstractClasses import Function, FunctionAssignments


# todo: here do you need to save the ID?
class FunctionStmNoParams(Function):
    def __init__(self, blockcode):
        self.stm = blockcode


class FunctionStm(Function):
    def __init__(self, function_assignments, blockcode):
        self.stm = function_assignments
        self.stm2 = blockcode


class FunctionAssignmentsStm(FunctionAssignments):
    def __init__(self, exp):
        self.stm = exp


class FunctionAssignmentsStmComma(FunctionAssignments):
    def __init__(self, exp, function_assignments):
        self.stm = exp
        self.stm2 = function_assignments