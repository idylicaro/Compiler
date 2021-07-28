from .AbstractVisitor import AbstractVisitor


class VisitorPrettyPrinter(AbstractVisitor):

    def visitInitCommandInit(self, initCommandInit):
        initCommandInit.stm.accept(self)
        print(';') # acho que não pode printar aqui, tem que printar dentro do proprio command
        initCommandInit.stm2.accept(self)

    def visitInitCommand(self, initCommand):
        initCommand.stm.accept(self)

    def visitInitFunctionInit(self, initFunctionInit):
        initFunctionInit.stm.accept(self)
        initFunctionInit.stm2.accept(self)

    def visitInitFunction(self, initFunction):
        initFunction.stm.accept(self)