from Tkinter import *
from os import system
from datetime import *
import speech_recognition

root = Tk()

def sayName(self):
    today = datetime.today()
    self.fntext = fnameEntry.get()
    self.lntext = lnameEntry.get()
    system('say Hello ' + self.fntext + self.lntext + ' . ')
    system('say The current date is: ' + str(today))

#Creates the Labels/Entry/Buttons Labels
fname = Label(root, text='First Name')
lname = Label(root, text='Last Name')
fnameEntry = Entry(root)
lnameEntry = Entry(root)
btnClick = Button(root, text='Talk to me!')

#Puts the Labels/Entry/Buttons in the Window
fname.grid(row=0)
lname.grid(row=1)
fnameEntry.grid(row=0, column=1)
lnameEntry.grid(row=1, column=1)
btnClick.grid(columnspan=2)

#Creates the event for the Button
btnClick.bind("<Button-1>", sayName)


root.mainloop()




