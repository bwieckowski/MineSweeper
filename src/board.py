import random

minSing = "m"

class Point:

    def __init__(self, x,y):
        self.coords = (x,y)

    def __add__(self, other):
        return Point(self.coords[0]+other.coords[0], self.coords[1]+other.coords[1])

    def __call__(self, i):
        return self.coords[i]

    def getX(self):
        return self.coords[0]

    def getY(self):
        return self.coords[1]

    def getCoords(self):
        return self.coords



class Board:

    outlineCoords = [Point(1, -1), Point(1, 0), Point(1, 1), Point(0, -1), Point(0, 1), Point(-1, -1), Point(-1, 0), Point(-1, 1)]
    findingZerosCoords = [Point(1, 0),Point(-1, 0),Point(0, 1),Point(0, -1)]

    def __init__(self, w, h, m ):

        self.minesCoords = set()
        self.width = w
        self.height = h
        self.mines = m

        self.__createGrid()
        self.__putMines()
        self.__putNumbers()

        self.zeros = [];



    def __createGrid(self):
        self.grid = [[ 0 for column in range(self.width) ] for row in range(self.height) ]


    def __putMines( self ):
        while self.mines > 0 :
            while True :
                i = random.randint(0, self.width - 1 )
                j = random.randint(0, self.height - 1)
                if self.grid[i][j] != minSing :
                    self.minesCoords.add(Point(i,j))
                    self.grid[i][j] = minSing
                    self.mines -= 1
                    break

    def findingZeros(self, point):
        if self.__validOutline(point):
            if self(point) == 0 and point.getCoords() not in self.zeros:
                self.zeros.append(point.getCoords())
                for item in self.findingZerosCoords:
                    newPoint = point + item
                    self.findingZeros(newPoint)
            else:
                return
        else:
            return
    def clearZeros( self ):
        self.zeros = []

    def getZerosFrom( self, point ):
        self.findingZeros(point)
        return self.zeros






    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def __validOutline(self, outlinePoint ):

        if outlinePoint(0) < 0 or outlinePoint(1) < 0  :
            return False

        if outlinePoint(0) > self.width-1 or outlinePoint(1) > self.height-1  :
            return False

        if self(outlinePoint) == minSing:
            return False

        return True


    def __putNumbers(self):
        for mine in self.minesCoords :
            for outline in self.outlineCoords:
                newPoint = outline+mine

                if self.__validOutline( newPoint ) :
                    self.grid[ newPoint(0) ][ newPoint(1) ] += 1

    def __call__(self, point):
        if(isinstance(point, Point )):
            return self.grid[point.getX()][point.getY()]
        else :
            return self.grid[point[0]][point[1]]


if __name__ == "__main__":

    board = Board( 4,4,2 )
    print(board())
