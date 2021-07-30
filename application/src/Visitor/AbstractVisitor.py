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

    @abstractmethod
    def visitCommandInterations(self, commandInterations):
        pass

    @abstractmethod
    def visitCommandExp(self, commandExp):
        pass
    @abstractmethod
    def visitCommandReturn(self, commandReturn):
        pass
    @abstractmethod
    def visitCommandBreak(self, commandBreak):
        pass
    @abstractmethod
    def visitCommandContinue(self, commandContinue):
        pass

    @abstractmethod
    def visitIfStm(self, ifStm):
        pass

    @abstractmethod
    def visitIfStatementBlockcode(self, ifStatementBlockcode):
        pass

    @abstractmethod
    def visitIfStatementBlockcodeElse(self, ifStatementBlockcodeElse):
        pass

    @abstractmethod
    def visitIfStatementBlockcodeElsif(self, ifStatementBlockcodeElsif):
        pass

    @abstractmethod
    def visitElsifStm(self, elsifStm):
        pass

    @abstractmethod
    def visitElsifStmElsif2(self, elsifStmElsif2):
        pass

    @abstractmethod
    def visitElsif2Elsif(self, elsif2Elsif):
        pass

    @abstractmethod
    def visitElsif2Else(self, elsif2Else):
        pass

    @abstractmethod
    def visitInterationsFor(self, interationsFor):
        pass

    @abstractmethod
    def visitInterationsDoWhile(self, interationsDoWhile):
        pass

    @abstractmethod
    def visitInterationsWhile(self, interationsDoWhile):
        pass

    @abstractmethod
    def visitInterationsWhileBlank(self, interationsDoWhile):
        pass

    @abstractmethod
    def visitForAssignmentsExp(self, forAssignmentsExp):
        pass

    @abstractmethod
    def visitForAssignmentsComma(self, forAssignmentsComma):
        pass

    @abstractmethod
    def visitCallStm(self, callStm):
        pass

    @abstractmethod
    def visitCallStmBlank(self, callStmBlank):
        pass

    @abstractmethod
    def visitReturnStm(self, returnStm):
        pass

    @abstractmethod
    def visitReturnStm(self, returnStm):
        pass

    @abstractmethod
    def visitExpAssignmentIdSc(self, expAssignmentIdSc):
        pass

    @abstractmethod
    def visitExpAssignmentIdLi(self, expAssignmentIdLi):
        pass

    @abstractmethod
    def visitExpAssignmentIdScMinus(self, expAssignmentIdScMinus):
        pass

    @abstractmethod
    def visitExpAssignmentIdScPlus(self, expAssignmentIdScPlus):
        pass
    @abstractmethod
    def visitExpAssignmentIdScMode(self, expAssignmentIdScMode):
        pass
    @abstractmethod
    def visitExpAssignmentIdScDivequal(self, expAssignmentIdScDivequal):
        pass
    @abstractmethod
    def visitExpAssignmentIdScTimes(self, expAssignmentIdScTimes):
        pass
    @abstractmethod
    def visitExpAssignmentLor(self, expAssignmentLor):
        pass

    @abstractmethod
    def visitExpLorStm(self, expLorStm):
        pass
    @abstractmethod
    def visitExpLorJustLand(self, expLorJustLand):
        pass
    @abstractmethod
    def visitExpLandStm(self, expLandStm):
        pass
    @abstractmethod
    def visitExpLandJustOr(self, expLandJustOr):
        pass
    @abstractmethod
    def visitExpOrStm(self, expOrStm):
        pass
    @abstractmethod
    def visitExpOrJustAnd(self, expOrJustAnd):
        pass
    @abstractmethod
    def visitExpAndStm(self, expAndStm):
        pass
    @abstractmethod
    def visitExpAndJustCompEq(self, expAndJustCompEq):
        pass
    @abstractmethod
    def visitExpCompEqEQ(self, expCompEqEQ):
        pass
    @abstractmethod
    def visitExpCompEqNE(self, expCompEqNE):
        pass
    @abstractmethod
    def visitExpCompEqSEQ(self, expCompEqSEQ):
        pass
    @abstractmethod
    def visitExpCompEqSNE(self, expCompEqSNE):
        pass
    @abstractmethod
    def visitExpCompEqCMP(self, expCompEqCMP):
        pass
    @abstractmethod
    def visitExpCompEqJust(self, expCompEqJust):
        pass
    @abstractmethod
    def visitExpCompGt(self, expCompGt):
        pass
    @abstractmethod
    def visitExpCompLt(self, expCompLt):
        pass
    @abstractmethod
    def visitExpCompGe(self, expCompGe):
        pass
    @abstractmethod
    def visitExpCompLe(self, expCompLe):
        pass
    @abstractmethod
    def visitExpCompSlt(self, expCompSlt):
        pass
    @abstractmethod
    def visitExpCompSgt(self, expCompSgt):
        pass
    @abstractmethod
    def visitExpCompSge(self, expCompSge):
        pass
    @abstractmethod
    def visitExpCompSle(self, expCompSle):
        pass
    @abstractmethod
    def visitExpCompJustPlus(self, expCompJustPlus):
        pass
    @abstractmethod
    def visitExpPlusMinusPlus(self, expPlusMinusPlus):
        pass
    @abstractmethod
    def visitExpPlusMinusMinus(self, expPlusMinusMinus):
        pass
    @abstractmethod
    def visitExpPlusMinusJustTimes(self, expPlusMinusJustTimes):
        pass
    @abstractmethod
    def visitExpTimesDividesTimes(self, expTimesDividesTimes):
        pass
    @abstractmethod
    def visitExpTimesDividesDivide(self, expTimesDividesDivide):
        pass
    @abstractmethod
    def visitExpTimesDividesModulo(self, expTimesDividesModulo):
        pass
    @abstractmethod
    def visitExpTimesDividesJustLnot(self, expTimesDividesJustLnot):
        pass
    @abstractmethod
    def visitExpLnotXor(self, expLnotXor):
        pass
    @abstractmethod
    def visitExpLnotJustDecrementIncrement(self, expLnotJustDecrementIncrement):
        pass
    @abstractmethod
    def visitExpDecrementPreIncrement(self, expDecrementPreIncrement):
        pass
    @abstractmethod
    def visitExpDecrementPosIncrement(self, expDecrementPosIncrement):
        pass
    @abstractmethod
    def visitExpDecrementPreDecrement(self, expDecrementPreDecrement):
        pass
    @abstractmethod
    def visitExpDecrementPosDecrement(self, expDecrementPosDecrement):
        pass
    @abstractmethod
    def visitExpDecrementIncrementJustLastLayer(self, expDecrementIncrementJustLastLayer):
        pass
    @abstractmethod
    def visitExpLastlayerExp(self, expLastlayerExp):
        pass
    @abstractmethod
    def visitExpLastlayerIdSc(self, expLastlayerIdSc):
        pass
    @abstractmethod
    def visitExpLastlayerIdLi(self, expLastlayerIdLi):
        pass
    @abstractmethod
    def visitExpLastlayerIdNumber(self, expLastlayerIdNumber):
        pass
    @abstractmethod
    def visitExpLastlayerCall(self, expLastlayerCall):
        pass
    @abstractmethod
    def visitExpLastlayerTrue(self, expLastlayerTrue):
        pass
    @abstractmethod
    def visitExpLastlayerFalse(self, expLastlayerFalse):
        pass
