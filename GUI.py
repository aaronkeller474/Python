from Tkinter import *
from os import system

root = Tk()

def sayName(event):
    system('say Hello ' + str(fnameEntry) + str(lnameEntry))

fname = Label(root, text='First Name')
lname = Label(root, text='Last Name')
fnameEntry = Entry(root)
lnameEntry = Entry(root)

fname.grid(row=0)
lname.grid(row=1)
fnameEntry.grid(row=0, column=1)
lnameEntry.grid(row=1, column=1)
btnClick = Button(root, text='Talk to me')
btnClick.bind("<Button-1>", sayName)
btnClick.grid(columnspan=2)

root.mainloop()




