from .AbstractVisitor import AbstractVisitor


class VisitorPrettyPrinter(AbstractVisitor):

    def visitInitCommandInit(self, initCommandInit):
        initCommandInit.stm.accept(self)
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
        print('sub')
        print(functionStmNoParams.id)
        print('()')
        print('{')
        functionStmNoParams.stm.accept(self)
        print('}')

    def visitFunctionStm(self, functionStm):
        print('sub')
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

    def visitInterationsFor(self, interationsFor):
        print('for')
        print('(')
        interationsFor.stm.accept(self)
        print(';')
        interationsFor.stm2.accept(self)
        print(';')
        interationsFor.stm3.accept(self)
        print(')')
        print('{')
        interationsFor.stm4.accept(self)
        print('}')

    def visitInterationsDoWhile(self, interationsDoWhile):
        print('do')
        print('{')
        interationsDoWhile.stm.accept(self)
        print('}')
        print('while')
        print('(')
        interationsDoWhile.stm2.accept(self)
        print(')')

    def visitInterationsWhile(self, interationsWhile):
        print('while')
        print('(')
        interationsWhile.stm.accept(self)
        print(')')
        print('{')
        interationsWhile.stm2.accept(self)
        print('}')

    def visitInterationsWhileBlank(self, interationsWhileBlank):
        print('while')
        print('(')
        interationsWhileBlank.stm.accept(self)
        print(')')
        print('{')
        print('}')

    def visitForAssignmentsExp(self, forAssignmentsExp):
        forAssignmentsExp.stm.accept(self)

    def visitForAssignmentsComma(self, forAssignmentsComma):
        forAssignmentsComma.stm.accept(self)
        print(',')
        forAssignmentsComma.stm2.accept(self)
