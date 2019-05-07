from  tkinter import *
from src.interface import Interface
from src.game import Game
from src.storage import Storage

root = Tk()

sotrage = Storage( )

interface = Interface( root )
game = Game(root )
interface.registerCallback( game.initGameCallBack )

root.mainloop()