from tkinter import *

def say_hi():
    print("hi there, everyone")

root = Tk()

#creates a frame widget
#frames can hold multiple other widgets
frame = Frame(root)
frame.pack()

#creates a button inside the frame widget
#button displays "QUIT"
#closes the window when clicked
quitButton = Button(frame, text = "QUIT", command=root.destroy)
quitButton.pack(side=LEFT)

#creates a button inside the frame widget
#button displays "HELLO"
#calls the say_hi function when clicked
hiButton = Button(frame, text="HELLO", command=say_hi)
hiButton.pack(side=LEFT)

root.mainloop





