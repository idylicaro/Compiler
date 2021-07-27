from .abstractClasses import Command


class CommandInterations(Command):
    def __init__(self, interation):
        self.stm = interation


class CommandIf(Command):
    def __init__(self, ifStm):
        self.stm = ifStm


class CommandExp(Command):
    def __init__(self, exp):
        self.stm = exp


class CommandCall(Command):
    def __init__(self, call):
        self.stm = call


class CommandReturn(Command):
    def __init__(self, returnStm):
        self.stm = returnStm


class CommandBreak(Command):
    def __init__(self, breakStm):
        self.stm = breakStm


class CommandContinue(Command):
    def __init__(self, continueStm):
        self.stm = continueStm
