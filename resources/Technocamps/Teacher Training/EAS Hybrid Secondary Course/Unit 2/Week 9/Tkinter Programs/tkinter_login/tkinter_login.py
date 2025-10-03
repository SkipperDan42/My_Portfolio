#########################################################
# This is the just the login that we did in the session #
#########################################################

from tkinter import *
from tkinter import messagebox

def tk_login():

	loginFrame = Frame(root)
	loginFrame.grid(row = 0, column = 0)

	titleLabel = Label(loginFrame, text = "Welcome to here!")
	titleLabel.grid(row = 0, column = 0)

	usernameLabel = Label(loginFrame, text = "username")
	usernameLabel.grid(row = 1, column = 0)
	usernameEntry = Entry(loginFrame)
	usernameEntry.grid(row = 1, column = 1)

	passwordLabel = Label(loginFrame, text = "password")
	passwordLabel.grid(row = 2, column = 0)
	passwordEntry = Entry(loginFrame)
	passwordEntry.grid(row = 2, column = 1)

	submitFrame = Frame(loginFrame)
	submitFrame.pack()
	submitButton = Button(loginFrame, text = "submit",
							bg = "White", fg = "Red",
							command = lambda: messagebox.showwarning("Yippee!","Yippee!") 
							if login(usernameEntry.get(), passwordEntry.get()) 
							else messagebox.showwarning("Failed!"))
	submitButton.grid(row = 3, column = 1)
	root.mainloop()


def login(inputted_username, inputted_password):
	stored_username = "dan"
	stored_password = "pass"

	if ((inputted_username == stored_username) and
		(inputted_password == stored_password)):
		print("\nWelcome!")
		return True
	else:
		print("\nWrong Username or Password!\n")
		return False

# Main Program running here
root = Tk()

tk_login()