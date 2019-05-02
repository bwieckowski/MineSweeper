from  tkinter import *
from src.interface import Interface


root = Tk()

interface = Interface( root )
interface.registerCallback( test )

root.mainloop()