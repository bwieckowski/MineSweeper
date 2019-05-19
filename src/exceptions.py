class Except(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))

    def getValue(self):
        return self.value


class NotDigitExceptions(Except):
    pass

class FieldSizeException(Except):
    pass

class EmptyFieldException(Except):
    pass

class MinesAmountException(Except):
    pass
