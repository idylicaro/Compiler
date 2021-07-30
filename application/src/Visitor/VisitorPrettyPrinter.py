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

    def visitCallStm(self, callStm):
        print(callStm.id)
        print('(')
        callStm.stm.accept(self)
        print(')')

    def visitCallStmBlank(self, callStmBlank):
        print(callStmBlank.id)
        print('()')

    def visitReturnStm(self, returnStm):
        returnStm.stm.accept(self)


    def visitExpAssignmentIdSc(self, expAssignmentIdSc):
        print(expAssignmentIdSc.id)
        print('=')
        expAssignmentIdSc.stm.accept(self)

    def visitExpAssignmentIdLi(self, expAssignmentIdLi):
        print(expAssignmentIdLi.id)
        print('=')
        expAssignmentIdLi.stm.accept(self)

    def visitExpAssignmentIdScMinus(self, expAssignmentIdScMinus):
        print(expAssignmentIdScMinus.id)
        print('-=')
        expAssignmentIdScMinus.stm.accept(self)

    def visitExpAssignmentIdScPlus(self, expAssignmentIdScPlus):
        print(expAssignmentIdScPlus.id)
        print('+=')
        expAssignmentIdScPlus.stm.accept(self)

    def visitExpAssignmentIdScMode(self, expAssignmentIdScMode):
        print(expAssignmentIdScMode.id)
        print('%=')
        expAssignmentIdScMode.stm.accept(self)

    def visitExpAssignmentIdScDivequal(self, expAssignmentIdScDivequal):
        print(expAssignmentIdScDivequal.id)
        print('/=')
        expAssignmentIdScDivequal.stm.accept(self)

    def visitExpAssignmentIdScTimes(self, expAssignmentIdScTimes):
        print(expAssignmentIdScTimes.id)
        print('*=')
        expAssignmentIdScTimes.stm.accept(self)

    def visitExpAssignmentLor(self, expAssignmentLor):
        expAssignmentLor.stm.accept(self)

    # todo: add prints...
    def visitExpLorStm(self, expLorStm):
        expLorStm.stm.accept(self)
        expLorStm.stm2.accept(self)

    def visitExpLorJustLand(self, expLorJustLand):
        expLorJustLand.stm.accept(self)

    def visitExpLandStm(self, expLandStm):
        expLandStm.stm.accept(self)
        expLandStm.stm2.accept(self)

    def visitExpLandJustOr(self, expLandJustOr):
        expLandJustOr.stm.accept(self)

    def visitExpOrStm(self, expOrStm):
        expOrStm.stm.accept(self)
        expOrStm.stm2.accept(self)

    def visitExpOrJustAnd(self, expOrJustAnd):
        expOrJustAnd.stm.accept(self)

    def visitExpAndStm(self, expAndStm):
        expAndStm.stm.accept(self)
        expAndStm.stm2.accept(self)

    def visitExpAndJustCompEq(self, expAndJustCompEq):
        expAndJustCompEq.stm.accept(self)

    def visitExpCompEqEQ(self, expCompEqEQ):
        expCompEqEQ.stm.accept(self)
        expCompEqEQ.stm2.accept(self)

    def visitExpCompEqNE(self, expCompEqNE):
        expCompEqNE.stm.accept(self)
        expCompEqNE.stm2.accept(self)

    def visitExpCompEqSEQ(self, expCompEqSEQ):
        expCompEqSEQ.stm.accept(self)
        expCompEqSEQ.stm2.accept(self)

    def visitExpCompEqSNE(self, expCompEqSNE):
        expCompEqSNE.stm.accept(self)
        expCompEqSNE.stm2.accept(self)

    def visitExpCompEqCMP(self, expCompEqCMP):
        expCompEqCMP.stm.accept(self)

    def visitExpCompEqJust(self, expCompEqJust):
        expCompEqJust.stm.accept(self)

    def visitExpCompGt(self, expCompGt):
        expCompGt.stm.accept(self)
        expCompGt.stm2.accept(self)

    def visitExpCompLt(self, expCompLt):
        expCompLt.stm.accept(self)
        expCompLt.stm2.accept(self)

    def visitExpCompGe(self, expCompGe):
        expCompGe.stm.accept(self)
        expCompGe.stm2.accept(self)

    def visitExpCompLe(self, expCompLe):
        expCompLe.stm.accept(self)
        expCompLe.stm2.accept(self)

    def visitExpCompSlt(self, expCompSlt):
        expCompSlt.stm.accept(self)
        expCompSlt.stm2.accept(self)

    def visitExpCompSgt(self, expCompSgt):
        expCompSgt.stm.accept(self)
        expCompSgt.stm2.accept(self)

    def visitExpCompSge(self, expCompSge):
        expCompSge.stm.accept(self)
        expCompSge.stm2.accept(self)

    def visitExpCompSle(self, expCompSle):
        expCompSle.stm.accept(self)
        expCompSle.stm2.accept(self)

    def visitExpCompJustPlus(self, expCompJustPlus):
        expCompJustPlus.stm.accept(self)

    def visitExpPlusMinusPlus(self, expPlusMinusPlus):
        expPlusMinusPlus.stm.accept(self)
        expPlusMinusPlus.stm2.accept(self)

    def visitExpPlusMinusMinus(self, expPlusMinusMinus):
        expPlusMinusMinus.stm.accept(self)
        expPlusMinusMinus.stm2.accept(self)

    def visitExpPlusMinusJustTimes(self, expPlusMinusJustTimes):
        expPlusMinusJustTimes.stm.accept(self)

    def visitExpTimesDividesTimes(self, expTimesDividesTimes):
        expTimesDividesTimes.stm.accept(self)
        expTimesDividesTimes.stm2.accept(self)

    def visitExpTimesDividesDivide(self, expTimesDividesDivide):
        expTimesDividesDivide.stm.accept(self)
        expTimesDividesDivide.stm2.accept(self)

    def visitExpTimesDividesModulo(self, expTimesDividesModulo):
        expTimesDividesModulo.stm.accept(self)
        expTimesDividesModulo.stm2.accept(self)

    def visitExpTimesDividesJustLnot(self, expTimesDividesJustLnot):
        expTimesDividesJustLnot.stm.accept(self)

    def visitExpLnotXor(self, expLnotXor):
        expLnotXor.stm.accept(self)

    def visitExpLnotJustDecrementIncrement(self, expLnotJustDecrementIncrement):
        expLnotJustDecrementIncrement.stm.accept(self)

    def visitExpDecrementPreIncrement(self, expDecrementPreIncrement):
        expDecrementPreIncrement.stm.accept(self)

    def visitExpDecrementPosIncrement(self, expDecrementPosIncrement):
        expDecrementPosIncrement.stm.accept(self)

    def visitExpDecrementPreDecrement(self, expDecrementPreDecrement):
        expDecrementPreDecrement.stm.accept(self)

    def visitExpDecrementPosDecrement(self, expDecrementPosDecrement):
        expDecrementPosDecrement.stm.accept(self)

    def visitExpDecrementIncrementJustLastLayer(self, expDecrementIncrementJustLastLayer):
        expDecrementIncrementJustLastLayer.stm.accept(self)

    def visitExpLastlayerExp(self, expLastlayerExp):
        expLastlayerExp.stm.accept(self)

    def visitExpLastlayerIdSc(self, expLastlayerIdSc):
        expLastlayerIdSc.stm.accept(self)

    def visitExpLastlayerIdLi(self, expLastlayerIdLi):
        expLastlayerIdLi.stm.accept(self)

    def visitExpLastlayerIdNumber(self, expLastlayerIdNumber):
        expLastlayerIdNumber.stm.accept(self)

    def visitExpLastlayerCall(self, expLastlayerCall):
        expLastlayerCall.stm.accept(self)

    def visitExpLastlayerTrue(self, expLastlayerTrue):
        expLastlayerTrue.stm.accept(self)

    def visitExpLastlayerFalse(self, expLastlayerFalse):
        expLastlayerFalse.stm.accept(self)