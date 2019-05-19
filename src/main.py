from tkinter import Tk, Image

from src.game import Game
from src.interface import Interface
from src.storage import Storage

storage = Storage()

root = Tk( )
root.title("Saper")
interface = Interface(root)
interface.pack()
game = Game(root)

interface.registerCallback( game.initGameCallBack )

root.mainloop()