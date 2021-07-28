from .abstractClasses import Blockcode


class BlockcodeCommand(Blockcode):
    def __init__(self, cmd):
        self.stm = cmd

    def accept(self, visitor):
        visitor.visitBlockcodeCommand(self)


class BlockcodeBcdCommand(Blockcode):
    def __init__(self, block, cmd):
        self.stm = block
        self.stm2 = cmd

    def accept(self, visitor):
        visitor.visitBlockcodeBcdCommand(self)
