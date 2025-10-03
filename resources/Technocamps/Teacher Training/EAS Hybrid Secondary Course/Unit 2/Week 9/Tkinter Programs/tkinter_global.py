#####################################################################
# This is a global variable version of we were doing in the session #
#####################################################################

from tkinter import *
from tkinter import messagebox



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
							command = lambda: tk_main(login_root) 
							if login(usernameEntry.get(), passwordEntry.get()) 
							else messagebox.showwarning("Failed!", "Failed!"))
	submitButton.grid(row = 3, column = 1)

	# The mainloop function keeps this GUI in a loop (i.e. keeps it active)
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



# This is the main tkinter program, displaying the shop
def tk_main(login_root):

	# In any function that uses global variables, we have to tell
	# it that it is allowed to do that, that is the one protection
	global items
	global totalSales

	# This time we pass the login WINDOW through from tk_login so that
	# we can destory the entire window here
	login_root.destroy()

	# And here is the main window,
	# created independently of the login window!
	main_root = Tk()

	# We create the new frame (whose parent is root),
	# and additionally the sub-frames (whose parent is the new frame)
	# that will hold the table and purchase information
	mainFrame = Frame(main_root)
	mainFrame.grid(row = 0, column = 0)
	tableFrame = Frame(mainFrame)
	tableFrame.grid(row = 1, column = 0)
	purchaseFrame = Frame(mainFrame)
	purchaseFrame.grid(row = 2, column = 0)

	# We populate the table frame with headers
	idLabel = Label(tableFrame, text = "Product ID").grid(row = 0, column = 0)
	nameLabel = Label(tableFrame, text = "Name").grid(row = 0, column = 1)
	priceLabel = Label(tableFrame, text = "Price (£)").grid(row = 0, column = 2)
	quantityLabel = Label(tableFrame, text = "Stock Level").grid(row = 0, column = 3)

	# Then we populate the purchase frame
	purchaseLabel = Label(purchaseFrame, text = "To Purchase: ")
	purchaseLabel.grid(row = 0, column = 0)
	purchaseEntry = Entry(purchaseFrame)
	purchaseEntry.grid(row = 0, column = 1)

	# Global variables makes adding our total sales very easy to do!
	# It is set up here, and refreshed within the update_stock() function
	salesLabel = Label(purchaseFrame, text = "Total Sales:")
	salesLabel.grid(row = 1, column = 1)
	salesValue = Label(purchaseFrame, text = str(f"{totalSales:.2f}"))
	salesValue.grid(row = 1,column = 2)

	# Then we populate the table with the *current* value of items
	# NOTE that we no longer need to pass items as it is GLOBAL
	# NOTE that we're doing this later so we can pass salesValue
	update_stock(tableFrame, salesValue)

	# The lambda function here has changed to only update_stock if the
	# purchase() is successful! 
	# Though, to be honest, using "else None" is also a dirty way to
	# program it. Here's where lambda functions fail and intermediary functions
	# are needed
	purchaseButton = Button(purchaseFrame, text = "Make Purchase",
							bg = "White", fg = "Blue",
							command = lambda: update_stock(tableFrame, salesValue) 
							if purchase(purchaseEntry.get())
							else None
							)
	purchaseButton.grid(row = 0, column = 2)

	# This is a new window so the mainloop() is now absolutely necessary!
	main_root.mainloop()



# This is the purchase function which handles whether a purchase can be made
# I don't like the fact we passes tableFrame into a method where it is largely
# irrelevant, so I will fix this in the decoupled-multiple-file program I make
def purchase(user_input):

	# As these are global we no longer need to pass them as parameters
	global items
	global totalSales
	try:
		key = int(user_input)

		if items[key]["Stock"] > 0:
			items[key]["Stock"] -= 1
			totalSales += items[key]["Price"]

			# NOTE instead of updating the stock here, the lambda function 
			# has chaged to only do that if purchase() returns True
			return True
		else:
			messagebox.showwarning("Out of Stock!", "Out of Stock")
			return False

	except (ValueError, KeyError):
		messagebox.showwarning("Enter a Valid Key!", "Enter a Valid Key!")
		return False



# This is update stock function that populates the table based on our items dictionary
# It now also updates the totalSales in the GUI
def update_stock(tableFrame, salesValue):

	# Again, this function may access our global variables, 
	# so we haven't passed them as parameters
	global items
	global totalSales

	# This fills in our table as before, we have passed the tableFrame as a parameter
	# as we do not need the Header Labels, just to add below them
	for i, item in enumerate(items):
		idLabel = Label(tableFrame, text = item).grid(row = i + 1, column = 0)
		nameLabel = Label(tableFrame, text = items[item]["Name"]).grid(row = i + 1, column = 1)
		priceLabel = Label(tableFrame, text = items[item]["Price"]).grid(row = i + 1, column = 2)
		quantityLabel = Label(tableFrame, text = items[item]["Stock"]).grid(row = i + 1, column = 3)

	# This updates the totalSales by editing the salesValue label
	salesValue.config(text = str(f"{totalSales:.2f}"))



# This is the load stock function that is currenty hardcoded
# - you can replace this to load from file (you will need a separate write to file)
def load_stock():
	items = {

			1: {"Name" : "Ben Shaw's D&B",
			  	"Price": 1.20,
			  	"Stock": 20
				},
			2: {"Name" : "Coca Cola",
			  	"Price": 1.50,
			  	"Stock": 100
				},
			3: {"Name" : "Irn Bru",
			  	"Price": 0.99,
			  	"Stock": 32
				},
			4: {"Name" : "R. White's Lemonade",
			  	"Price": 1.20,
			  	"Stock": 57
				}
			}

	return items


# We define desired global variables as such. Now they can be accessed
# anywhere at any time! Dangerous, but easier...
# Beware because: 1) easier to cause problems
#				  2) harder to debug
#				  3) WJEC *may* not like it 
global items
global totalSales

# We initialise our now global variables as usual
items = load_stock()
totalSales = 0

# NOTE That at this point we could also create both windows,
# and leave main unpopulated until after login...

# We kick off our program by calling the login function
tk_login()
