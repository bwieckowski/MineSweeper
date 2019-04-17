from  tkinter import *



def showText() :
    print( mField.get())
    print(nField.get())

root = Tk()
label = Label(root, text="test xD ")
mField = Entry(root)
nField = Entry(root)



buttin = Button(root,text="Call me", command =  lambda: showText())
label.pack()
mField.pack()
nField.pack()
buttin.pack()

root.mainloop()