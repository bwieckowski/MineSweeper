from tkinter import Label, PhotoImage

from src.myLabel import MyLabel


class Tile( MyLabel ) :

    def __init__(self, root, point ):
        self.__flagLevel = 0
        self.__active = True
        self.__isFlagged = False
        super(Tile, self ).__init__( root )

        self.point = point
        self.setImage("../res/images/blank.gif")
        self.bind("<Button-1>", self.action)
        self.bind("<Button-2>", self.flag)

    def isActive(self):
        return self.__active

    def getFlagLevel(self):
        return self.__flagLevel

    def disActive(self):
        self.__active = False

    def open(self):
        if self.__flagLevel == 0:
            self.setImage(self.underphoto)

    def action(self,event):
        self.open()

    def getCoords(self):
        return self.point.getCoords()


    def flag(self, event):
        if self.__active :

            if  self.__flagLevel == 0 :
                self.__flagLevel = 1
                self.setImage("../res/images/bombflagged.gif")
                self.__isFlagged = True

            elif self.__flagLevel == 1 :
                self.__flagLevel = 2
                self.setImage("../res/images/bombquestion.gif")
                self.__isFlagged = True

            else  :
                self.__flagLevel = 0
                self.setImage("../res/images/blank.gif")
                self.__isFlagged = False




class Bomb( Tile ) :

    def __init__(self, root, point ):
            Tile.__init__( self, root, point )
            self.underphoto = "../res/images/bombrevealed.gif"

    def shade(self):
        if  self.getFlagLevel() == 0:
            self.setImage("../res/images/blankShaded.gif")


    def boom(self):
        self.setImage("../res/images/bombdeath.gif")


class Number( Tile ):

    def __init__(self, root, point,value ):
        self.__value = value
        Tile.__init__( self, root, point )
        self.underphoto = "../res/images/open" + str(value) + ".gif"

    def getValue(self):
        return self.__value



class TileFactory :
    def getTile(self, root, type, point ):
        tile = None
        if type == "m":
            tile = Bomb( root, point )
        else:
            tile = Number( root,point, type )
        return tile
