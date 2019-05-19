from src.exceptions import *


class Validation:

    def size(self, width, height, mines):
        self.status = False
        if width == "" or height == "" or mines == "" :
            raise EmptyFieldException( "Wypełnij wszyskie pola" )

        if width.isdigit()  and height.isdigit() and mines.isdigit() :
            width = int(width)
            height = int(height)
            mines = int(mines)
        else :
            raise NotDigitExceptions(" Wpisz liczbę ")

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

        self.status = True