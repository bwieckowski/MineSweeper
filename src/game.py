from src.board import Board
from tkinter import Frame, Tk, PhotoImage, Label

from src.storage import Storage
from src.tile import Tile


class Game( Frame ):

    def __init__(self, root ):
        super(Game,self).__init__()

    def initGameCallBack(self):
        storage = Storage()
        m  = storage.get( "mines" )
        h = storage.get( "height" )
        w = storage.get( "width" )

        self.board = Board( w,h,m )
        self.__createFrame()




    def __createFrame(self):

        for row in range(len(self.board())):
            for column in range(len(self.board()[row])) :

                tile = Tile( self, self.board()[row][column] )
                tile.grid(row=row, column=column)

        self.pack()

if  __name__ == "__main__" :
    storage = Storage()
    storage.add("mines",2)
    storage.add("height",4)
    storage.add("width",4)

    root = Tk()
    game = Game(root)
    game.initGameCallBack()


    root.mainloop()