from .abstractClasses import Exp, ExpOr, ExpAnd, ExpLor, ExpLand, ExpLnot, ExpComp, ExpCompEq, ExpPlusMinus, \
    ExpTimesDivides, ExpDecrementIncrement, ExpLastLayer


class ExpAssignmentIdSc(Exp):
    def __init__(self, id, exp_lor):
        self.id = id
        self.stm2 = exp_lor

    def accept(self, visitor):
        visitor.visitExpAssignmentIdSc(self)

class ExpAssignmentIdLi(Exp):
    def __init__(self, id, exp_lor):
        self.id = id
        self.stm2 = exp_lor

    def accept(self, visitor):
        visitor.visitExpAssignmentIdLi(self)

class ExpAssignmentIdScMinus(Exp):
    def __init__(self, id, exp_lor):
        self.id = id
        self.stm2 = exp_lor

    def accept(self, visitor):
        visitor.visitExpAssignmentIdScMinus(self)

class ExpAssignmentIdScPlus(Exp):
    def __init__(self, id, exp_lor):
        self.id = id
        self.stm2 = exp_lor

    def accept(self, visitor):
        visitor.visitExpAssignmentIdScPlus(self)

class ExpAssignmentIdScMode(Exp):
    def __init__(self, id, exp_lor):
        self.id = id
        self.stm2 = exp_lor

    def accept(self, visitor):
        visitor.visitExpAssignmentIdScMode(self)

class ExpAssignmentIdScDivequal(Exp):
    def __init__(self, id, exp_lor):
        self.id = id
        self.stm2 = exp_lor

    def accept(self, visitor):
        visitor.visitExpAssignmentIdScDivequal(self)

class ExpAssignmentIdScTimes(Exp):
    def __init__(self, id, exp_lor):
        self.id = id
        self.stm2 = exp_lor

    def accept(self, visitor):
        visitor.visitExpAssignmentIdScTimes(self)

class ExpAssignmentLor(Exp):
    def __init__(self, exp_lor):
        self.stm = exp_lor

    def accept(self, visitor):
        visitor.visitExpAssignmentLor(self)


class ExpLorStm(ExpLor):
    def __init__(self, exp_lor, exp_land):
        self.stm = exp_lor
        self.stm2 = exp_land

    def accept(self, visitor):
        visitor.visitExpLorStm(self)

class ExpLorJustLand(ExpLor):
    def __init__(self, exp_land):
        self.stm = exp_land

    def accept(self, visitor):
        visitor.visitExpLorJustLand(self)


class ExpLandStm(ExpLand):
    def __init__(self, exp_land, exp_or):
        self.stm = exp_land
        self.stm2 = exp_or

    def accept(self, visitor):
        visitor.visitExpLandStm(self)

class ExpLandJustOr(ExpLand):
    def __init__(self, exp_or):
        self.stm = exp_or

    def accept(self, visitor):
        visitor.visitExpLandJustOr(self)

class ExpOrStm(ExpOr):
    def __init__(self, exp_or, exp_and):
        self.stm = exp_or
        self.stm2 = exp_and

    def accept(self, visitor):
        visitor.visitExpOrStm(self)

class ExpOrJustAnd(ExpOr):
    def __init__(self, exp_and):
        self.stm = exp_and

    def accept(self, visitor):
        visitor.visitExpOrJustAnd(self)

class ExpAndStm(ExpAnd):
    def __init__(self, exp_and, exp_comp_eq):
        self.stm = exp_and
        self.stm2 = exp_comp_eq

    def accept(self, visitor):
        visitor.visitExpAndStm(self)

class ExpAndJustCompEq(ExpAnd):
    def __init__(self, exp_comp_eq):
        self.stm = exp_comp_eq

    def accept(self, visitor):
        visitor.visitExpAndJustCompEq(self)

class ExpCompEqEQ(ExpCompEq):
    def __init__(self, expComp, expComp2):
        self.stm = expComp
        self.stm2 = expComp2

    def accept(self, visitor):
        visitor.visitExpCompEqEQ(self)

class ExpCompEqNE(ExpCompEq):
    def __init__(self, expComp, expComp2):
        self.stm = expComp
        self.stm2 = expComp2

    def accept(self, visitor):
        visitor.visitExpCompEqNE(self)

class ExpCompEqSEQ(ExpCompEq):
    def __init__(self, expComp, expComp2):
        self.stm = expComp
        self.stm2 = expComp2

    def accept(self, visitor):
        visitor.visitExpCompEqSEQ(self)

class ExpCompEqSNE(ExpCompEq):
    def __init__(self, expComp, expComp2):
        self.stm = expComp
        self.stm2 = expComp2

    def accept(self, visitor):
        visitor.visitExpCompEqSNE(self)

class ExpCompEqCMP(ExpCompEq):
    def __init__(self, expComp, expComp2):
        self.stm = expComp
        self.stm2 = expComp2

    def accept(self, visitor):
        visitor.visitExpCompEqCMP(self)

class ExpCompEqJust(ExpCompEq):
    def __init__(self, expComp):
        self.stm = expComp

    def accept(self, visitor):
        visitor.visitExpCompEqJust(self)

class ExpCompGt(ExpComp):
    def __init__(self, expComp, expCompPlus):
        self.stm = expComp
        self.stm2 = expCompPlus

    def accept(self, visitor):
        visitor.visitExpCompGt(self)

class ExpCompLt(ExpComp):
    def __init__(self, expComp, expCompPlus):
        self.stm = expComp
        self.stm2 = expCompPlus

    def accept(self, visitor):
        visitor.visitExpCompLt(self)

class ExpCompGe(ExpComp):
    def __init__(self, expComp, expCompPlus):
        self.stm = expComp
        self.stm2 = expCompPlus

    def accept(self, visitor):
        visitor.visitExpCompGe(self)

class ExpCompLe(ExpComp):
    def __init__(self, expComp, expCompPlus):
        self.stm = expComp
        self.stm2 = expCompPlus

    def accept(self, visitor):
        visitor.visitExpCompLe(self)

class ExpCompSlt(ExpComp):
    def __init__(self, expComp, expCompPlus):
        self.stm = expComp
        self.stm2 = expCompPlus

    def accept(self, visitor):
        visitor.visitExpCompSlt(self)

class ExpCompSgt(ExpComp):
    def __init__(self, expComp, expCompPlus):
        self.stm = expComp
        self.stm2 = expCompPlus

    def accept(self, visitor):
        visitor.visitExpCompSgt(self)

class ExpCompSge(ExpComp):
    def __init__(self, expComp, expCompPlus):
        self.stm = expComp
        self.stm2 = expCompPlus

    def accept(self, visitor):
        visitor.visitExpCompSge(self)

class ExpCompSle(ExpComp):
    def __init__(self, expComp, expCompPlus):
        self.stm = expComp
        self.stm2 = expCompPlus

    def accept(self, visitor):
        visitor.visitExpCompSle(self)

class ExpCompJustPlus(ExpComp):
    def __init__(self, expCompPlus):
        self.stm = expCompPlus

    def accept(self, visitor):
        visitor.visitExpCompJustPlus(self)

class ExpPlusMinusPlus(ExpPlusMinus):
    def __init__(self, exp_plus_minus, exp_times_divides):
        self.stm = exp_plus_minus
        self.stm2 = exp_times_divides

    def accept(self, visitor):
        visitor.visitExpPlusMinusPlus(self)

class ExpPlusMinusMinus(ExpPlusMinus):
    def __init__(self, exp_plus_minus, exp_times_divides):
        self.stm = exp_plus_minus
        self.stm2 = exp_times_divides

    def accept(self, visitor):
        visitor.visitExpPlusMinusMinus(self)

class ExpPlusMinusJustTimes(ExpPlusMinus):
    def __init__(self, exp_times_divides):
        self.stm = exp_times_divides

    def accept(self, visitor):
        visitor.visitExpPlusMinusJustTimes(self)

class ExpTimesDividesTimes(ExpTimesDivides):
    def __init__(self, exp_times_divides, exp_lnot):
        self.stm = exp_times_divides
        self.stm2 = exp_lnot

    def accept(self, visitor):
        visitor.visitExpTimesDividesTimes(self)

class ExpTimesDividesDivide(ExpTimesDivides):
    def __init__(self, exp_times_divides, exp_lnot):
        self.stm = exp_times_divides
        self.stm2 = exp_lnot

    def accept(self, visitor):
        visitor.visitExpTimesDividesDivide(self)

class ExpTimesDividesModulo(ExpTimesDivides):
    def __init__(self, exp_times_divides, exp_lnot):
        self.stm = exp_times_divides
        self.stm2 = exp_lnot

    def accept(self, visitor):
        visitor.visitExpTimesDividesModulo(self)

class ExpTimesDividesJustLnot(ExpTimesDivides):
    def __init__(self, exp_lnot):
        self.stm = exp_lnot

    def accept(self, visitor):
        visitor.visitExpTimesDividesJustLnot(self)

class ExpLnotXor(ExpLnot):
    def __init__(self, exp_lnot):
        self.stm = exp_lnot

    def accept(self, visitor):
        visitor.visitExpLnotXor(self)

class ExpLnotJustDecrementIncrement(ExpLnot):
    def __init__(self, exp_decrement_increment):
        self.stm = exp_decrement_increment

    def accept(self, visitor):
        visitor.visitExpLnotJustDecrementIncrement(self)

class ExpDecrementPreIncrement(ExpDecrementIncrement):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        visitor.visitExpDecrementPreIncrement(self)

class ExpDecrementPosIncrement(ExpDecrementIncrement):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        visitor.visitExpDecrementPosIncrement(self)

class ExpDecrementPreDecrement(ExpDecrementIncrement):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        visitor.visitExpDecrementPreDecrement(self)

class ExpDecrementPosDecrement(ExpDecrementIncrement):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        visitor.visitExpDecrementPosDecrement(self)

class ExpDecrementIncrementJustLastLayer(ExpLastLayer):
    def __init__(self, exp_lastlayer):
        self.stm = exp_lastlayer

    def accept(self, visitor):
        visitor.visitExpDecrementIncrementJustLastLayer(self)

class ExpLastlayerExp(ExpLastLayer):
    def __init__(self, exp):
        self.stm = exp

    def accept(self, visitor):
        visitor.visitExpLastlayerExp(self)

class ExpLastlayerIdSc(ExpLastLayer):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        visitor.visitExpLastlayerIdSc(self)

class ExpLastlayerIdLi(ExpLastLayer):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        visitor.visitExpLastlayerIdLi(self)

class ExpLastlayerIdNumber(ExpLastLayer):
    def __init__(self, num):
        self.num = num

    def accept(self, visitor):
        visitor.visitExpLastlayerIdNumber(self)

class ExpLastlayerCall(ExpLastLayer):
    def __init__(self, call):
        self.stm = call

    def accept(self, visitor):
        visitor.visitExpLastlayerCall(self)

class ExpLastlayerTrue(ExpLastLayer):
    def accept(self, visitor):
        visitor.visitExpLastlayerTrue(self)


class ExpLastlayerFalse(ExpLastLayer):
    def accept(self, visitor):
        visitor.visitExpLastlayerFalse(self)
