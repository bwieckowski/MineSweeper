
class FieldSizeException(Exception):

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return (repr(self.value))

        def getValue(self):
            return self.value


class MinesAmountException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))

    def getValue(self):
        return self.value
