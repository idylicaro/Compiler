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