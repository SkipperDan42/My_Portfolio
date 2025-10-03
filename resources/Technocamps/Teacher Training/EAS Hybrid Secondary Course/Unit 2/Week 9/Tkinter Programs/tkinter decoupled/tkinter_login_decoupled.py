from tkinter import *
from tkinter import messagebox
from tkinter_core_decoupled import *

# This is the tkinter login screen GUI
def tk_login():

	# For extra differences I have created two seperate windows
	# for the main and login screens in this example
	login_root = Tk()

	# We create our login frame from the root window,
	# and define it to use the grid manager
	loginFrame = Frame(login_root)
	loginFrame.grid(row = 0, column = 0)

	# We create a nice title at the top of our window
	titleLabel = Label(loginFrame, text = "Welcome to here!")
	titleLabel.grid(row = 0, column = 0)

	# We create the username label and text-entry fields
	usernameLabel = Label(loginFrame, text = "username")
	usernameLabel.grid(row = 1, column = 0)
	usernameEntry = Entry(loginFrame)
	usernameEntry.grid(row = 1, column = 1)

	# We create the password label and text-entry fields
	passwordLabel = Label(loginFrame, text = "password")
	passwordLabel.grid(row = 2, column = 0)
	passwordEntry = Entry(loginFrame)
	passwordEntry.grid(row = 2, column = 1)

	# We create a button that calls the login function with a lambda function,
	# This will only run tk_main() if the login function returns True
	submitButton = Button(loginFrame, text = "submit",
							bg = "White", fg = "Red",
							command = lambda: login_success(login_root) 
							if login(usernameEntry.get(), passwordEntry.get()) 
							else messagebox.showwarning("Failed!", "Failed!"))
	submitButton.grid(row = 3, column = 1)

	# The main loop function keeps theis GUI in a loop (i.e. keeps it active)
	# and waiting for user input - we need this at the end of every new window
	login_root.mainloop()



# This function handles the actual login check, after pressing the button
def login(inputted_username, inputted_password):
	stored_username = "dan"
	stored_password = "pass"

	if ((inputted_username == stored_username) and
		(inputted_password == stored_password)):
		return True
	else:
		return False



# If the login was successful then we run this function to both -
# Delete this window - and -
# Call the Core Program
def login_success(login_root):
	# We pass the login frame through from tk_login so that we can
	# destory it here
	login_root.destroy()

	# Now we launch the core program 
	# (avoiding calling it main - as main just launches everything)
	tk_core()

