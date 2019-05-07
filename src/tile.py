from tkinter import Button, PhotoImage


class Tile( Button ) :

    def __init__(self, root, type, row ):
        self.type = type
        photo=PhotoImage(file= "../res/images/blank.gif")
        super(Tile, self).__init__(  image=photo)
        self.grid(row = row )
