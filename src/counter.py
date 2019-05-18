from threading import Thread
from tkinter import Tk, Frame, PhotoImage, TOP, LEFT, RIGHT

import time

from src.myLabel import MyLabel


class Counter( Frame ):

    def __init__(self, root ):
        self.root = root
        super(Counter, self).__init__()
        self.display = [ ]
        self.setVal(1)



    def setVal(self, val):
        self.value = val
        self.updateFront()

    def up(self):
        self.value += 1
        self.updateFront()

    def down(self):
        self.value -= 1
        self.updateFront()

    def getArray(self, value ):
        now = 10
        tab = []
        tmp = value
        while tmp > 0:
            tab.append(int((tmp % now) * 10 / now))

            tmp = tmp - tmp % now
            now = now * 10
        if tab == [] :
            tab = [0]
        tab.reverse()
        return tab

    def getPhotoUrl(self, number):
        url = "../res/images/time"+str(number)+".gif"
        return url

    def updateFront(self):
        array = self.getArray(self.value)

        if len(array) == 1:
            array.insert(0, 0)


        while len( self.display ) != len( array ) :
            label = MyLabel(self)
            self.display.append(label)

        for i in  range( len(array) ) :
            photo = self.getPhotoUrl( array[i] )
            label = self.display[i]
            label.setImage( photo )
            label.pack( side=LEFT )


class MyTimer( Counter):

    def __init__(self, root ):
        super(MyTimer, self).__init__( root )
        self.root = root
        self.isGoing = 0;
        self.reset()

    def tick(self):
        self.up()
        if self.isGoing == 1 :
            self.root.after(1000, self.tick)


    def start(self):
        self.isGoing = 1
        self.root.after(1000, self.tick)

    def stop(self):
        self.isGoing = 0

    def reset(self):
        self.setVal(0)

class MineCounter( Counter ):
    pass



if __name__ == "__main__" :


    root = Tk()

    t = MyTimer(root)
    t.start()


    root.mainloop()