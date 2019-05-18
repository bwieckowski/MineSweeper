from tkinter import Label, PhotoImage

from src.myLabel import MyLabel


class Tile( MyLabel ) :

    def __init__(self, root, type, point ):
        self.flagLevel = 0
        self.active = True
        super(Tile, self ).__init__( root )
        self.type = type
        self.point = point
        self.setImage("../res/images/blank.gif")
        self.bind("<Button-1>", self.action)
        self.bind("<Button-2>", self.flag)

    def isActive(self):
        return self.active

    def disActive(self):
        self.active = False

    def open(self):
        if self.flagLevel == 0:
            self.setImage(self.underphoto)

    def action(self,event):
        self.open()

    def getCoords(self):
        return self.point.getCoords()


    def flag(self, event):
        if self.active :

            if  self.flagLevel == 0 :
                self.flagLevel = 1
                self.setImage("../res/images/bombflagged.gif")

            elif self.flagLevel == 1 :
                self.flagLevel = 2
                self.setImage("../res/images/bombquestion.gif")

            else  :
                self.flagLevel = 0
                self.setImage("../res/images/blank.gif")
                self.isFlagged = False




class Bomb( Tile ) :

    def __init__(self, root, point ):
            Tile.__init__( self, root, "m", point )
            self.underphoto = "../res/images/bombdeath.gif"

    def shade(self):
        self.setImage("../res/images/blankShaded.gif")


class Number( Tile ):

    def __init__(self, root, type, point ):
        Tile.__init__( self, root, type, point )
        self.underphoto = "../res/images/open" + str(type) + ".gif"



class TileFactory :
    def getTile(self, root, type, point ):
        tile = None
        if type == "m":
            tile = Bomb( root, point )
        else:
            tile = Number( root, type,point )
        return tile
