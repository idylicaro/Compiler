from .AbstractVisitor import AbstractVisitor


class VisitorPrettyPrinter(AbstractVisitor):

    def visitInitCommandInit(self, initCommandInit):
        initCommandInit.stm.accept(self)
        print(';')  # acho que não pode printar aqui, tem que printar dentro do proprio command
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
        # todo: o id ele chama o accept ou da um print apenas ?
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

    def visitCommandInterations(self, commandInterations):
        commandInterations.stm.accept(self)

    def visitCommandExp(self, commandExp):
        commandExp.stm.accept(self)
        print(';')

    def visitCommandReturn(self, commandReturn):
        print('return')
        commandReturn.stm.accept(self)
        print(';')

    def visitCommandBreak(self, commandBreak):
        commandBreak.stm.accept(self)
        print(';')

    def visitCommandContinue(self, commandContinue):
        commandContinue.stm.accept(self)
        print(';')

    def visitIfStm(self, ifStm):
        print('if')
        print('(')
        ifStm.stm.accept(self)
        print(')')
        ifStm.stm2.accept(self)

    def visitIfStatementBlockcode(self, ifStatementBlockcode):
        print('{')
        ifStatementBlockcode.stm.accept(self)
        print('}')

    def visitIfStatementBlockcodeElse(self, ifStatementBlockcodeElse):
        print('{')
        ifStatementBlockcodeElse.stm.accept(self)
        print('}')
        print('else')
        print('{')
        ifStatementBlockcodeElse.stm2.accept(self)
        print('}')

    def visitIfStatementBlockcodeElsif(self, ifStatementBlockcodeElsif):
        print('{')
        ifStatementBlockcodeElsif.stm.accept(self)
        print('}')
        ifStatementBlockcodeElsif.stm2.accept(self)

    def visitElsifStm(self, elsifStm):
        print('elsif')
        print('(')
        elsifStm.stm.accept(self)
        print(')')
        print('{')
        elsifStm.stm2.accept(self)
        print('}')

    def visitElsifStmElsif2(self, elsifStmElsif2):
        print('elsif')
        print('(')
        elsifStmElsif2.stm.accept(self)
        print(')')
        print('{')
        elsifStmElsif2.stm2.accept(self)
        print('}')
        elsifStmElsif2.stm3.accept(self)

    def visitElsif2Elsif(self, elsif2Elsif):
        elsif2Elsif.stm.accept(self)

    def visitElsif2Else(self, elsif2Else):
        print('else')
        print('{')
        elsif2Else.stm.accept(self)
        print('}')
