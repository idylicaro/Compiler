from abc import ABC, abstractmethod

class AbstractVisitor(ABC):
    pass

    @abstractmethod
    def visitInitCommandInit(self, commandInit):
        pass