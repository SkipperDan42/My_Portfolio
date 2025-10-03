###########################################################
# This is the just the login based on the pack() function # 
# in the WJEC sample paper                                #
###########################################################

from tkinter import *

def tk_login():

	usernameFrame = Frame(loginFrame)
	usernameFrame.pack()
	usernameLabel = Label(usernameFrame, text = "Username: ")
	usernameLabel.pack(side=LEFT)
	usernameEntry = Entry(usernameFrame)
	usernameEntry.pack(side=RIGHT)


	passwordFrame = Frame(loginFrame)
	passwordFrame.pack()
	passwordLabel = Label(passwordFrame, text = "Password: ")
	passwordLabel.pack(side=LEFT)
	passwordEntry = Entry(passwordFrame)
	passwordEntry.pack(side=RIGHT)

	submitFrame = Frame(loginFrame)
	submitFrame.pack()
	submitButton = Button(submitFrame, text = "submit",
							bg = "White", fg = "Red",
							command = lambda:login(usernameEntry.get(), passwordEntry.get()))
	submitButton.pack()
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


root = Tk()
loginFrame = Frame(root)
loginFrame.pack()

tk_login()