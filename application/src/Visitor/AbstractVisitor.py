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