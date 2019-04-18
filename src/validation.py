from src.exceptions import FieldSizeException, MinesAmountException


class Validation:

    def size(self, width, height, mines):

        if width < 2:
            raise FieldSizeException("Za mała szerokość pola")

        if height < 2:
            raise FieldSizeException("Za mała wysokość pola")

        if width > 15:
            raise FieldSizeException("Za duża szerokość pola")

        if height > 15:
            raise FieldSizeException("Za duża wysokość pola")

        if mines <= 0:
            raise MinesAmountException("Za mała liczba min")

        if mines >= height*width:
            raise MinesAmountException("Za duża liczba min")
