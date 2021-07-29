from abc import ABC, abstractmethod

class AbstractVisitor(ABC):

    @abstractmethod
    def visitInitCommandInit(self, InitCommandInit):
        pass

    @abstractmethod
    def visitInitCommand(self, commandInit):
        pass

    @abstractmethod
    def visitInitFunctionInit(self, initFunctionInit):
        pass

    @abstractmethod
    def visitInitFunction(self, initFunction):
        pass

    @abstractmethod
    def visitBlockcodeCommand(self, blockcodeCommand):
        pass

    @abstractmethod
    def visitBlockcodeBcdCommand(self, blockcodeBcdCommand):
        pass

    @abstractmethod
    def visitFunctionStmNoParams(self, functionStmNoParams):
        pass

    @abstractmethod
    def visitFunctionStm(self, functionStm):
        pass

    @abstractmethod
    def visitFunctionAssignmentsStm(self, functionAssignmentsStm):
        pass

    @abstractmethod
    def visitFunctionAssignmentsStmComma(self, functionAssignmentsStmComma):
        pass

    @abstractmethod
    def visitCommandInterations(self, commandInterations):
        pass

    @abstractmethod
    def visitCommandExp(self, commandExp):
        pass
    @abstractmethod
    def visitCommandReturn(self, commandReturn):
        pass
    @abstractmethod
    def visitCommandBreak(self, commandBreak):
        pass
    @abstractmethod
    def visitCommandContinue(self, commandContinue):
        pass

    @abstractmethod
    def visitIfStm(self, ifStm):
        pass

    @abstractmethod
    def visitIfStatementBlockcode(self, ifStatementBlockcode):
        pass

    @abstractmethod
    def visitIfStatementBlockcodeElse(self, ifStatementBlockcodeElse):
        pass

    @abstractmethod
    def visitIfStatementBlockcodeElsif(self, ifStatementBlockcodeElsif):
        pass

    @abstractmethod
    def visitElsifStm(self, elsifStm):
        pass

    @abstractmethod
    def visitElsifStmElsif2(self, elsifStmElsif2):
        pass

    @abstractmethod
    def visitElsif2Elsif(self, elsif2Elsif):
        pass

    @abstractmethod
    def visitElsif2Else(self, elsif2Else):
        pass