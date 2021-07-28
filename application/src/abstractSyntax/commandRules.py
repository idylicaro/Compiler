from .abstractClasses import Command


class CommandInterations(Command):
    def __init__(self, interation):
        self.stm = interation

    def accept(self, visitor):
        visitor.visitCommandInterations(self)


class CommandExp(Command):
    def __init__(self, exp):
        self.stm = exp

    def accept(self, visitor):
        visitor.visitCommandExp(self)


class CommandReturn(Command):
    def __init__(self, returnStm):
        self.stm = returnStm

    def accept(self, visitor):
        visitor.visitCommandReturn(self)

class CommandBreak(Command):
    def __init__(self, breakStm):
        self.stm = breakStm

    def accept(self, visitor):
        visitor.visitCommandBreak(self)

class CommandContinue(Command):
    def __init__(self, continueStm):
        self.stm = continueStm

    def accept(self, visitor):
        visitor.visitCommandContinue(self)