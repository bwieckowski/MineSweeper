from threading import Timer

from src.board import Board, Point
from tkinter import Frame, Tk, PhotoImage, Label, LEFT, RIGHT, TOP, BOTTOM, W, X, YES, BOTH

from src.counter import MyTimer, Counter
from src.storage import Storage
from src.tile import Tile, Bomb, Number, TileFactory


class Game( Frame ):

    def __init__(self, root ):
        super(Game,self).__init__()


    def initGameCallBack(self):
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



        self.bind_class('Label', '<Button-1>', self.openTileEvent)
        self.bind_class('Label', '<Button-2>', self.flagTile)
        root.bind('<KeyPress>', self.keyboardEvent)

        self.code =""
        self.initInterface()
        self.__createFrame()


    def bounce(self ):
         self.code = ""

    def keyboardEvent(self, event):
            self.startGame()
            self.code = self.code + event.char
            if self.code == "xyzzy":
                self.showAllMines()
            Timer(1.5, self.bounce).start()

    def showAllMines(self):
        print("showing...")
        for tile in self.bombs :
            tile.shade()

    def initInterface(self):
        frame = Frame( self )
        self.timer = MyTimer( frame )
        self.timer.pack(side=RIGHT)

        self.counter = Counter( frame )
        self.counter.pack( side = LEFT)
        self.counter.setVal( self.mines )

        frame.pack(side=TOP, anchor=W, fill=X, expand=YES)

    def startGame(self):
        if not self.isGameStarted:
            self.timer.start()
            self.isGameStarted = True

    def win(self):
        print("koniec Gry - wygrałeś")
        self.timer.stop()

    def gameOver(self):
        print("koniec Gry - przegrałeś")
        self.timer.stop()

    def openTileEvent(self, event):


        self.startGame()

        if self.tilesAmount == self.mines:
            self.win()

        tile = event.widget
        point = tile.point

        if not tile.isActive():
            print( tile.isActive( ) )
            return

        tile.disActive()
        if isinstance( tile, Bomb) and tile.flagLevel == 0:
            self.gameOver()

        if tile.type == 0 :
                zeros = self.board.getZerosFrom( point )
                print( self.tiles )
                for zero in zeros :
                    tmpTile =self.tiles[zero[0]][zero[1]]
                    tmpTile.open()
                    tmpTile.disActive()
                    self.tilesAmount -= 1
                self.board.clearZeros()
        else:
            self.tilesAmount -= 1
            print(self.tilesAmount)
            self.checkTilesAmount()



    def newPrediction(self, bomb ):
        self.bombsPrediction.add( bomb)
        newSet = self.bombs - self.bombsPrediction
        if not len(newSet) :
            self.win()

    def flagTile( self, event ):

        self.startGame()

        if event.widget.flagLevel == 1 :
            self.counter.down()
            self.newPrediction( event.widget )

        elif event.widget.flagLevel == 2 :
            self.counter.up()
            self.bombsPrediction.remove( event.widget )





    def __createFrame(self ):

        tileFactory = TileFactory()
        frame = Frame( self )


        for row in range(self.board.getWidth()):
            for column in range(self.board.getHeight()) :
                point = Point(row, column)
                type = self.board( point )
                tile = tileFactory.getTile(frame, type , point  )

                if isinstance(tile, Bomb):
                    self.bombs.add(tile)

                self.tiles[row][column] = tile
                tile.grid(row=row, column=column)

        frame.pack(side=TOP, anchor=W, fill=X, expand=YES)


    def checkTilesAmount(self):
        if self.tilesAmount == self.mines :
            self.win()


if  __name__ == "__main__" :

    storage = Storage()
    storage.add("mines",3)
    storage.add("height",20)
    storage.add("width",20)

    root = Tk()
    game = Game(root)
    game.initGameCallBack()
    game.pack(fill=BOTH, expand=YES)


    root.mainloop()