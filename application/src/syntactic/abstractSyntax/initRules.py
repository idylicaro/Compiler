from abstractClasses import Init


class InitCommandInit(Init):
    def __init__(self, cmd, init):
        self.stm = cmd
        self.stm2 = init


class InitCommand(Init):
    def __init__(self, cmd):
        self.stm = cmd


class InitFunctionInit(Init):
    def __init__(self, func, init):
        self.stm = func
        self.stm2 = init


class InitFunction(Init):
    def __init__(self, func):
        self.stm = func
