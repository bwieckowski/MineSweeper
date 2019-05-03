import random

minSing = "m"

class Point:
    def __init__(self, x,y):
        self.coords = (x,y)

    def __add__(self, other):
        return (self.coords[0]+other.coords[0], self.coords[1]+other.coords[1])

    def __call__(self, *args, **kwargs):
        return self.coords

class Board:

    def __init__(self, w, h ):
        self.minesCoords = set()
        self.width = w
        self.height = h

        self.outlineCoords = [ Point(1,-1), Point(1,0), Point(1,1) , Point(0,-1), Point(0,1),Point( -1,-1), Point(-1,0), Point(-1,1) ]

    def init(self, w,h, m):
        self.createGrid( )
        self.putMines( m )
        self.putNumbers()


    def createGrid(self):
        self.grid = [[ 0 for column in range(self.width) ] for row in range(self.height) ]


    def putMines(self, m ):
        while m > 0 :
            while True :
                i = random.randint(0, self.width - 1 )
                j = random.randint(0, self.height - 1)
                if self.grid[i][j] != minSing :
                    self.minesCoords.add(Point(i,j))
                    self.grid[i][j] = minSing
                    m -= 1
                    break


    def validOutline(self, outline):

        if outline[0] < 0 or outline[1] <0  :
            return False

        if outline[0] > self.width-1 or outline[1] > self.height-1  :
            return False

        if self.grid[outline[0]][outline[1]] == minSing:
            return False

        return True


    def putNumbers(self):
        for mine in self.minesCoords :
            for outline in self.outlineCoords:
                newPoint = outline+mine
                if self.validOutline( newPoint ) :
                    self.grid[ newPoint[0] ][ newPoint[1] ] += 1


    def getBoard(self):
        return self.grid


if __name__ == "__main__":
    board = Board( 4,4 )
    board.createGrid( )
    board.putMines( 2 )
    board.putNumbers()
    print(board.getBoard())
