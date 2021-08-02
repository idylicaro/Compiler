from .abstractClasses import Continue, Break


class ContinueStm(Continue):
    def accept(self, visitor):
        visitor.visitContinueStm(self)



class BreakStm(Break):
    def accept(self, visitor):
        visitor.visitBreakStm(self)
