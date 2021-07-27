from .abstractClasses import Call


class CallStm(Call):
    def __init__(self, id, function_assignments):
        self.id = id
        self.stm = function_assignments


class CallStmBlank(Call):
    def __init__(self, id):
        self.id = id
