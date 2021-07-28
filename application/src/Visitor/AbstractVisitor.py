from abc import ABC, abstractmethod

class AbstractVisitor(ABC):

    @abstractmethod
    def visitInitCommandInit(self, commandInit):
        pass