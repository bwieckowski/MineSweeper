from src.board import Board
from tkinter import Frame, Tk, Button, PhotoImage

from src.storage import Storage
from src.tile import Tile


class Game( Frame ):

    def __init__(self, root ):
        super(Game,self).__init__()
        Frame.__init__( root )

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
                print(row+column)
                photo = PhotoImage(file= "time9.gif")
                tile = Button( self,image=photo,text="A",width="20",height="20",activebackground="red",activeforeground="red" )   #Tile( self, self.board()[row][column], row )
                tile.grid(row=row,column=column )
        self.pack()

if  __name__ == "__main__" :
    storage = Storage()
    storage.add("mines",3)
    storage.add("height",10)
    storage.add("width",10)

    root = Tk()
    game = Game(root)
    game.initGameCallBack()

    root.mainloop()