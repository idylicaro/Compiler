from .abstractClasses import Interations, For, ForAssignments, DoWhile, While


class InterationsFor(Interations):
    def __init__(self, for_assignments, exp, for_assignments2, blockcode):
        self.stm = for_assignments
        self.stm2 = exp
        self.stm3 = for_assignments2
        self.stm4 = blockcode

    def accept(self, visitor):
        visitor.visitInterationsFor(self)

class InterationsDoWhile(Interations):
    def __init__(self, blockcode, exp):
        self.stm = blockcode
        self.stm2 = exp

    def accept(self, visitor):
        visitor.visitInterationsDoWhile(self)

class InterationsWhile(Interations):
    def __init__(self, exp, blockcode):
        self.stm = exp
        self.stm2 = blockcode

    def accept(self, visitor):
        visitor.visitInterationsWhile(self)

class InterationsWhileBlank(While):
    def __init__(self, exp):
        self.stm = exp

    def accept(self, visitor):
        visitor.visitInterationsWhileBlank(self)

class ForAssignmentsExp(ForAssignments):
    def __init__(self, exp):
        self.stm = exp

    def accept(self, visitor):
        visitor.visitForAssignmentsExp(self)

class ForAssignmentsComma(ForAssignments):
    def __init__(self, exp, for_assignments):
        self.stm = exp
        self.stm2 = for_assignments

    def accept(self, visitor):
        visitor.visitForAssignmentsComma(self)

