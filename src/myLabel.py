from tkinter import PhotoImage, Label


class MyLabel( Label ) :

    def __init__(self,  root):
       super(MyLabel, self).__init__( root,bd=0,  highlightthickness=0 )

    def setImage(self, url):
        photo = PhotoImage(file=url)
        self.config(image=photo)
        self.image = photo
