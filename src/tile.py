from tkinter import Label, PhotoImage


class Tile( Label ) :

    def action(self,event):
        if not self.isFlagged:
            self.config( image=self.underphoto )
            self.image = self.underphoto
            self.isCovered = False
        return "break"

    def flag(self, event):

        if self.isCovered :
            if  not self.isFlagged :
                self.isFlagged = True
                flagged = PhotoImage(file="../res/images/bombflagged.gif")
                self.config(image= flagged)
                self.image = flagged
            else  :
                photo = PhotoImage(file="../res/images/blank.gif")
                self.config(image=photo)
                self.image = photo
                self.isFlagged = False



    def __init__(self, root, type ):
        self.isFlagged = False
        self.isCovered = True

        self.type = type
        photo=PhotoImage(file= "../res/images/blank.gif")

        if type == "m" :
            self.underphoto = PhotoImage(file= "../res/images/bombrevealed.gif")
        else :
            url = "../res/images/open"+str(type)+".gif"
            self.underphoto = PhotoImage(file=url)

        super(Tile, self).__init__( root, image=photo,bd=0,highlightthickness = 0 )
        self.image = photo
        self.pack()
        self.bind("<Button-1>", self.action)
        self.bind("<Button-2>", self.flag)

