from .AbstractVisitor import AbstractVisitor


class VisitorPrettyPrinter(AbstractVisitor):

    def visitInitCommandInit(self, initCommandInit):
        initCommandInit.stm.accept(self)
        print(';')
        initCommandInit.stm2.accept(self)


