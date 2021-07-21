from abstractClasses import Call


# todo: here do you need to save the ID?

class CallStm(Call):
    def __init__(self, function_assignments):
        self.stm = function_assignments


class CallStmBlank(Call):
    pass
