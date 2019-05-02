import random

class Board:

    def __init__(self):
        self.minesCoords = set()

    def init(self, w,h, m):

        self.createGrid(w,h)
        self.putMines( m )
        self.putNumbers()


    def createGrid(self,w,h):
        self.grid = [[ 0 for column in range(w) ] for row in range( h )]

    def putMines(self, m ):
        while m > 0 :
            while True :
                i = random.randint(0, len(self.grid)-1)
                j = random.randint(0, len(self.grid[0])-1)
                if self.grid[i][j] != "m" :
                    self.minesCoords.add((i,j))
                    self.grid[i][j] = "m"
                    m -= 1
                    break
        print(self.grid)
        print(self.minesCoords)




board = Board()
board.createGrid( 3,2 )
