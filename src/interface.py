from tkinter import *
from tkinter import messagebox

from src.storage import Storage
from src.validation import Validation


class Interface( Frame ):


    def __init__(self, parent):

        self.validator = Validation()
        Frame.__init__(self,parent)

        self.callbacks = []
        self.parent = parent
        heightLabel = Label(self, text="wysokość").grid(row=0)
        self.heightEntry = Entry(self)
        self.heightEntry.grid(row=0, column=1)

        widthLabel = Label(self, text="szerokość").grid(row=1)
        self.widthEntry = Entry(self)
        self.widthEntry.grid(row=1, column=1)

        minesLabel = Label(self, text="miny").grid(row=2)
        self.minesEntry = Entry(self)
        self.minesEntry.grid(row=2, column=1)

        button = Button(self, text="Start Game", command=lambda: self.callFunctions() ).grid(row=3, column=0, padx=10)
        exit = Button(self, text="Exit", command=parent.destroy).grid(row=3, column=2,padx=10,)
        self.pack( pady=10)

    def callFunctions(self):
        self.initValues()
        if self.validator.status :
            for fun in self.callbacks:
                fun()

        self.parent.focus()

    def registerCallback(self, fun ):
        self.callbacks.append( fun )

    def initValues(self) :

        try:
            self.validator.size( self.widthEntry.get(), self.heightEntry.get(), self.minesEntry.get())

        except Exception as exc:
            self.widthEntry.delete(0, 'end')
            self.heightEntry.delete(0, 'end')
            self.minesEntry.delete(0, 'end')

            messagebox.showerror("Error", str(exc.getValue()))


        else:
            self.width = int(self.widthEntry.get())
            self.height = int(self.widthEntry.get())
            self.mines = int(self.minesEntry.get())

            storage = Storage()

            storage.add("mines",self.mines)
            storage.add("height", self.height)
            storage.add("width",self.width)
            print("Save in storage")



