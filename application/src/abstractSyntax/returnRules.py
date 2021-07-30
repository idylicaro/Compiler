from .abstractClasses import Return


class ReturnStm(Return):
    def __init__(self, exp):
        self.stm = exp

    def accept(self, visitor):
        visitor.visitCommandReturn(self)