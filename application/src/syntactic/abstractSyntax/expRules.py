from abstractClasses import Exp, ExpOr, ExpAnd, ExpLor, ExpLand, ExpLnot, ExpComp, ExpCompEq, ExpPlusMinus, \
    ExpTimesDivides, ExpDecrementIncrement, ExpLastLayer


class ExpAssignmentIdSc(Exp):
    def __init__(self, id, exp_lor):
        self.id = id
        self.stm2 = exp_lor


class ExpAssignmentIdLi(Exp):
    def __init__(self, id, exp_lor):
        self.id = id
        self.stm2 = exp_lor


class ExpAssignmentIdScMinus(Exp):
    def __init__(self, id, exp_lor):
        self.id = id
        self.stm2 = exp_lor


class ExpAssignmentIdScPlus(Exp):
    def __init__(self, id, exp_lor):
        self.id = id
        self.stm2 = exp_lor


class ExpAssignmentIdScMode(Exp):
    def __init__(self, id, exp_lor):
        self.id = id
        self.stm2 = exp_lor


class ExpAssignmentIdScTimes(Exp):
    def __init__(self, id, exp_lor):
        self.id = id
        self.stm2 = exp_lor


class ExpAssignmentLor(Exp):
    def __init__(self, exp_lor):
        self.stm = exp_lor


class ExpLor(Exp):
    def __init__(self, exp_lor, exp_land):
        self.stm = exp_lor
        self.stm2 = exp_land


class ExpLorJustLand(Exp):
    def __init__(self, exp_land):
        self.stm2 = exp_land


class ExpLand(Exp):
    def __init__(self, exp_land, exp_or):
        self.stm = exp_land
        self.stm2 = exp_or


class ExpLandJustOr(Exp):
    def __init__(self, exp_or):
        self.stm = exp_or


class ExpOr(Exp):
    def __init__(self, exp_or, exp_and):
        self.stm = exp_or
        self.stm2 = exp_and


class ExpOrJustAnd(Exp):
    def __init__(self, exp_and):
        self.stm = exp_and


class ExpAnd(Exp):
    def __init__(self, exp_and, exp_comp_eq):
        self.stm = exp_and
        self.stm2 = exp_comp_eq


class ExpAndJustCompEq(Exp):
    def __init__(self, exp_comp_eq):
        self.stm = exp_comp_eq


class ExpCompEqEQ(Exp):
    def __init__(self, expComp, expComp2):
        self.expComp = expComp
        self.expComp2 = expComp2


class ExpCompEqNE(Exp):
    def __init__(self, expComp, expComp2):
        self.expComp = expComp
        self.expComp2 = expComp2


class ExpCompEqSEQ(Exp):
    def __init__(self, expComp, expComp2):
        self.expComp = expComp
        self.expComp2 = expComp2


class ExpCompEqSNE(Exp):
    def __init__(self, expComp, expComp2):
        self.expComp = expComp
        self.expComp2 = expComp2


class ExpCompEqCMP(Exp):
    def __init__(self, expComp, expComp2):
        self.expComp = expComp
        self.expComp2 = expComp2


class ExpCompEqJust(Exp):
    def __init__(self, expComp):
        self.expComp = expComp


class ExpCompGt(Exp):
    def __init__(self, expComp, expCompPlus):
        self.stm = expComp
        self.stm2 = expCompPlus


class ExpCompLt(Exp):
    def __init__(self, expComp, expCompPlus):
        self.stm = expComp
        self.stm2 = expCompPlus


class ExpCompLe(Exp):
    def __init__(self, expComp, expCompPlus):
        self.stm = expComp
        self.stm2 = expCompPlus


class ExpCompSlt(Exp):
    def __init__(self, expComp, expCompPlus):
        self.stm = expComp
        self.stm2 = expCompPlus


class ExpCompSgt(Exp):
    def __init__(self, expComp, expCompPlus):
        self.stm = expComp
        self.stm2 = expCompPlus


class ExpCompSge(Exp):
    def __init__(self, expComp, expCompPlus):
        self.stm = expComp
        self.stm2 = expCompPlus


class ExpCompSle(Exp):
    def __init__(self, expComp, expCompPlus):
        self.stm = expComp
        self.stm2 = expCompPlus


class ExpCompJustPlus(Exp):
    def __init__(self, expCompPlus):
        self.stm = expCompPlus


class ExpPlusMinusPlus(ExpPlusMinus):
    def __init__(self, exp_plus_minus, exp_times_divides):
        self.stm = exp_plus_minus
        self.stm2 = exp_times_divides


class ExpPlusMinusMinus(ExpPlusMinus):
    def __init__(self, exp_plus_minus, exp_times_divides):
        self.stm = exp_plus_minus
        self.stm2 = exp_times_divides


class ExpPlusMinusJustTimes(ExpPlusMinus):
    def __init__(self, exp_times_divides):
        self.stm = exp_times_divides


class ExpTimesDividesTimes(ExpTimesDivides):
    def __init__(self, exp_times_divides, exp_lnot):
        self.stm = exp_times_divides
        self.stm2 = exp_lnot


class ExpTimesDividesDivide(ExpTimesDivides):
    def __init__(self, exp_times_divides, exp_lnot):
        self.stm = exp_times_divides
        self.stm2 = exp_lnot


class ExpTimesDividesModulo(ExpTimesDivides):
    def __init__(self, exp_times_divides, exp_lnot):
        self.stm = exp_times_divides
        self.stm2 = exp_lnot


class ExpTimesDividesJustLnot(ExpTimesDivides):
    def __init__(self, exp_lnot):
        self.stm = exp_lnot


class ExpLnotXor(ExpLnot):
    def __init__(self, exp_lnot):
        self.stm = exp_lnot


class ExpLnotJustDecrementIncrement(ExpLnot):
    def __init__(self, exp_decrement_increment):
        self.stm = exp_decrement_increment


class ExpDecrementPreIncrement(ExpDecrementIncrement):
    def __init__(self, id):
        self.id = id


class ExpDecrementPosIncrement(ExpDecrementIncrement):
    def __init__(self, id):
        self.id = id


class ExpDecrementPreDecrement(ExpDecrementIncrement):
    def __init__(self, id):
        self.id = id


class ExpDecrementPosDecrement(ExpDecrementIncrement):
    def __init__(self, id):
        self.id = id


class ExpDecrementIncrementJustLastLayer(ExpLastLayer):
    def __init__(self, exp_lastlayer):
        self.stm = exp_lastlayer


class ExpLastlayerExp(ExpLastLayer):
    def __init__(self, exp):
        self.stm = exp


class ExpLastlayerIdSc(ExpLastLayer):
    def __init__(self, id):
        self.id = id


class ExpLastlayerIdLi(ExpLastLayer):
    def __init__(self, id):
        self.id = id


class ExpLastlayerIdNumber(ExpLastLayer):
    def __init__(self, num):
        self.num = num


class ExpLastlayerCall(ExpLastLayer):
    def __init__(self, call):
        self.call = call


class ExpLastlayerTrue(ExpLastLayer):
    pass
    # def __init__(self, call):
    #     self.call = call


class ExpLastlayerFalse(ExpLastLayer):
    pass
