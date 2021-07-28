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

    def visitBlockcodeCommand(self, blockcodeCommand):
        blockcodeCommand.stm.accept(self)

    def visitBlockcodeBcdCommand(self, blockcodeBcdCommand):
        blockcodeBcdCommand.stm.accept(self)
        blockcodeBcdCommand.stm2.accept(self)

    def visitFunctionStmNoParams(self, functionStmNoParams):
        #todo: o id ele chama o accept ou da um print apenas ?
        print('sub')
        # functionStmNoParams.id.accept(self)
        print(functionStmNoParams.id)
        print('()')
        print('{')
        functionStmNoParams.stm.accept(self)
        print('}')

    def visitFunctionStm(self, functionStm):
        print('sub')
        # functionStm.id.accept(self)
        print(functionStm.id)
        print('(')
        functionStm.stm.accept(self)
        print(')')
        print('{')
        functionStm.stm2.accept(self)
        print('}')

    def visitFunctionAssignmentsStm(self, functionAssignmentsStm):
        functionAssignmentsStm.stm.accept(self)

    def visitFunctionAssignmentsStmComma(self, functionAssignmentsStmComma):
        functionAssignmentsStmComma.stm.accept(self)
        print(',')
        functionAssignmentsStmComma.stm2.accept(self)