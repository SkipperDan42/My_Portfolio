from tkinter import *
from tkinter import messagebox

username = "guest"
password = "admin"

def login(usernameEntry, passwordEntry):
    if username == usernameEntry and password == passwordEntry:
        print("Welcome")
    else:
        messagebox.showwarning("ERROR", "Invalid username password combination")


root = Tk()

#creates a frame widget
#frames can hold multiple other widgets
frame = Frame(root)
frame.grid(row=0, column=0)

#creates another frame inside the original
#will be useful later to extend the functionality of our GUI
loginFrame=Frame(frame)
loginFrame.grid(row=0, column=0)

#creates username label and entry widgets
#sets their position within the loginFrame
usernameLabel=Label(loginFrame, text="username")
usernameLabel.grid(row=0, column=0)
usernameEntry=Entry(loginFrame)
usernameEntry.grid(row=0, column=1)

#creates password label and entry widgets
#sets their position within the loginFrame
passwordLabel=Label(loginFrame, text="password")
passwordLabel.grid(row=1, column=0)
passwordEntry=Entry(loginFrame)
passwordEntry.grid(row=1, column=1)

#creates a submit button
#sets its position within the loginFrame
submitButton=Button(loginFrame, text="submit",
                    command=lambda:login(usernameEntry.get(), passwordEntry.get()))
submitButton.grid(row=2, column=1)

root.mainloop()
 




