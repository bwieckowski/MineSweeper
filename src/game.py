from threading import Timer

from src.board import Board, Point
from tkinter import Frame, Tk, PhotoImage, Label, LEFT, RIGHT, TOP, BOTTOM, W, X, YES, BOTH, Y, messagebox

from src.counter import MyTimer, Counter
from src.storage import Storage
from src.tile import Tile, Bomb, Number, TileFactory


class Game(  ):

    def __init__(self, root ):
        self.root = root
        self.gameFrame = ""
        self.interFrame = ""


    def initGameCallBack(self):


        if isinstance( self.interFrame, Frame) :
            self.interFrame.destroy()
            self.timer.destroy()
            self.counter.destroy()

        if isinstance(self.gameFrame, Frame):
            self.gameFrame.destroy()

        storage = Storage()
        self.mines  = storage.get( "mines" )
        h = storage.get( "height" )
        w = storage.get( "width" )
        self.isGameStarted = False

        self.tiles = [[j for j in range(w)] for i in range(h)]
        self.bombs = set()
        self.bombsPrediction = set()
        self.tilesAmount = w*h

        self.board = Board( w,h,self.mines )



        self.root.bind_class('Label', '<Button-1>', self.openTileEvent)
        self.root.bind_class('Label', '<Button-2>', self.flagTileEvent)
        self.root.bind('<KeyPress>', self.keyboardEvent)

        self.code =""
        self.__createFrame()
        self.__initInterface()



    def showAll(self):
        for i in self.tiles:
            for tile in i :
                tile.open()
                if not isinstance( tile, Bomb) and tile.getFlagLevel() != 0:
                    tile.setImage("../res/images/bombmisflagged.gif")

    def showAllMines(self):
        print("showing...")
        for tile in self.bombs :
            tile.shade()


    def __initInterface(self):
        self.interFrame = Frame( self.root, bg="green" )
        self.timer = MyTimer( self.interFrame  )
        self.timer.pack( side = LEFT, padx=20)

        self.counter = Counter( self.interFrame  )
        self.counter.setVal( self.mines )
        self.counter.pack( side = RIGHT, padx=20)
        self.interFrame.pack()


    def __createFrame(self ):

        tileFactory = TileFactory()
        self.gameFrame = Frame( self.root )

        for row in range(self.board.getWidth()):
            for column in range(self.board.getHeight()) :
                point = Point(row, column)
                type = self.board( point )
                tile = tileFactory.getTile(self.gameFrame, type , point  )
                if isinstance(tile, Bomb):
                    self.bombs.add(tile)

                self.tiles[row][column] = tile
                tile.grid(row=row, column=column)
        self.gameFrame.pack( side=BOTTOM, padx=20, pady=20)




    def startGame(self):
        if not self.isGameStarted:
            self.timer.start()
            self.isGameStarted = True



    def keyboardEvent(self, event):
            self.startGame()
            self.code = self.code + event.char
            if self.code == "xyzzy":
                self.showAllMines()
            Timer(2, self.bounce).start()


    def bounce(self ):
         self.code = ""


    def flagTileEvent( self, event ):

        self.startGame()

        if event.widget.getFlagLevel() == 1 :
            self.counter.down()
            self.newPrediction( event.widget )

        elif event.widget.getFlagLevel() == 2 :
            self.counter.up()
            self.bombsPrediction.remove( event.widget )




    def openTileEvent(self, event):


        self.startGame()

        if self.tilesAmount == self.mines:
            self.win( "wygrałeś")

        tile = event.widget
        point = tile.point

        if not tile.isActive():
            return

        tile.disActive()

        if isinstance( tile, Bomb) and tile.getFlagLevel() == 0:
            self.root.after(10,tile.boom)
            self.gameOver("przegrałeś")

        if isinstance(tile,Number) and tile.getValue() == 0 :
                zeros = self.board.getZerosFrom( point )
                for zero in zeros :
                    tmpTile =self.tiles[zero[0]][zero[1]]
                    tmpTile.open()
                    tmpTile.disActive()
                    self.tilesAmount -= 1
                self.board.clearZeros()
        else:
            self.tilesAmount -= 1
            self.checkTilesAmount()


    def checkTilesAmount(self):
        if self.tilesAmount == self.mines :
            self.gameOver("wygrałeś")

    def newPrediction(self, bomb ):
        self.bombsPrediction.add( bomb)
        newSet = self.bombs - self.bombsPrediction
        if not len(newSet) :
            self.gameOver("wygrałeś")








    def gameOver(self, text):
        self.timer.stop()
        self.showAll()
        messagebox.showerror("koniec Gry", text)



if  __name__ == "__main__" :

    storage = Storage()
    storage.add("mines",3)
    storage.add("height",20)
    storage.add("width",20)

    root = Tk()
    game = Game(root)
    game.initGameCallBack()


    root.mainloop()