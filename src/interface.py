from tkinter import *
from tkinter import messagebox

from src.validation import Validation


class Interface( Frame ):


    def __init__(self, parent):


        Frame.__init__(self,parent)

        self.callbacks = []
        self.callbacks.append( self.initValues )

        heightLabel = Label(self, text="wysokość").grid(row=0)
        self.heightEntry = Entry(self)
        self.heightEntry.grid(row=0, column=1)

        widthLabel = Label(self, text="szerokość").grid(row=1)
        self.widthEntry = Entry(self)
        self.widthEntry.grid(row=1, column=1)

        minesLabel = Label(self, text="miny").grid(row=2)
        self.minesEntry = Entry(self)
        self.minesEntry.grid(row=2, column=1)

        buttin = Button(self, text="Call me", command=lambda: self.callFunctions() ).grid(row=3)

        self.pack()

    def callFunctions(self):
        for fun in self.callbacks:
            fun()

    def registerCallback(self, fun ):
        self.callbacks.append( fun )

    def initValues(self) :

        try:
            validator = Validation()
            validator.size( int(self.widthEntry.get()), int(self.heightEntry.get()), int(self.minesEntry.get()))

        except Exception as exc:
            messagebox.showerror("Error", str(exc.getValue()))

        else:
            self.width = self.widthEntry.get()
            self.height = self.widthEntry.get()
            self.mines = self.minesEntry.get()
        finally:
            print( self.widthEntry.get() )


