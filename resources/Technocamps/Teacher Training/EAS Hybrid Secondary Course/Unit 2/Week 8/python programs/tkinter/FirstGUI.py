#imports tkinter module
from tkinter import *

#initialising tkinter with a root widget
#provides an empty window that we can fill
#create only one root widget for each program
#must be created before other widgets
root = Tk()

#creates a label widget inside the root widget
#label will display "Hello world!"
label = Label(root, text="Hello world!")

#pack method tells the label to size itself
label.pack()

#tkinter event loop
#opens the window
#program remains in the loop until the window is closed
root.mainloop()



