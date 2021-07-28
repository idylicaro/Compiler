from .abstractClasses import Init


class InitCommandInit(Init):
    def __init__(self, cmd, init):
        self.stm = cmd
        self.stm2 = init

    def accept(self, visitor):
        visitor.visitInitCommandInit(self)


class InitCommand(Init):
    def __init__(self, cmd):
        self.stm = cmd

    def accept(self, visitor):
        visitor.visitInitCommand(self)


class InitFunctionInit(Init):
    def __init__(self, func, init):
        self.stm = func
        self.stm2 = init

    def accept(self, visitor):
        visitor.visitInitFunctionInit(self)


class InitFunction(Init):
    def __init__(self, func):
        self.stm = func

    def accept(self, visitor):
        visitor.visitInitFunction(self)