from abstractClasses import Blockcode


class BlockcodeCommand(Blockcode):
    def __init__(self, cmd):
        self.stm = cmd


class BlockcodeBcdCommand(Blockcode):
    def __init__(self, block, cmd):
        self.stm = block
        self.stm2 = cmd
