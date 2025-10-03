################################################################
# This is the full implementation based on the pack() function # 
# in the WJEC sample paper                                     #
################################################################

from tkinter import *
from tkinter import messagebox



# This is the tkinter login screen GUI
def tk_login():

	# We create our login frame from the root window,
	# and define it to use the grid manager
	loginFrame = Frame(root)
	loginFrame.pack()

	# We create a nice title at the top of our window
	titleFrame = Frame(loginFrame)
	titleFrame.pack()
	titleLabel = Label(titleFrame, text = "Welcome to here!")
	titleLabel.pack()

	# We create the username label and text-entry fields
	usernameFrame = Frame(loginFrame)
	usernameFrame.pack()
	usernameLabel = Label(usernameFrame, text = "username")
	usernameLabel.pack(side = LEFT)
	usernameEntry = Entry(usernameFrame)
	usernameEntry.pack(side = RIGHT)

	# We create the password label and text-entry fields
	passwordFrame = Frame(loginFrame)
	passwordFrame.pack()
	passwordLabel = Label(passwordFrame, text = "Password: ")
	passwordLabel.pack(side=LEFT)
	passwordEntry = Entry(passwordFrame)
	passwordEntry.pack(side=RIGHT)

	# We create a button that calls the login function with a lambda function,
	# This will only run tk_main() if the login function returns True
	submitButton = Button(loginFrame, text = "submit",
							bg = "White", fg = "Red",
							command = lambda: tk_main(loginFrame) 
							if login(usernameEntry.get(), passwordEntry.get()) 
							else messagebox.showwarning("Failed!", "Failed!"))
	submitButton.pack()

	# The main loop function keeps theis GUI in a loop (i.e. keeps it active)
	# and waiting for user input - we need this at the end of every new window
	# - see tk_main()
	root.mainloop()



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
def tk_main(loginFrame):
	# We pass the login frame through from tk_login so that we can
	# destory it here
	loginFrame.destroy()

	# We initialise our shop variables when opening the main program
	items = load_stock()
	totalSales = 0

	# We create the new frame (whose parent is root),
	# and additionally the sub-frames (whose parent is the new frame)
	# that will hold the table and purchase information
	mainFrame = Frame(root)
	mainFrame.pack()
	tableFrame = Frame(mainFrame)
	tableFrame.pack(side = TOP)
	purchaseFrame = Frame(mainFrame)
	purchaseFrame.pack(side = BOTTOM)

	# We now populate the table frame with a frame for EVERY column, 
	# this is just to keep the table structure intact!
	id_column_frame = Frame(tableFrame)
	id_column_frame.pack(side = LEFT)
	idLabel = Label(id_column_frame, text = "Product ID")
	idLabel.pack(side = TOP)

	name_column_frame = Frame(tableFrame)
	name_column_frame.pack(side = LEFT)
	nameLabel = Label(name_column_frame, text = "Name")
	nameLabel.pack(side = TOP)

	price_column_frame = Frame(tableFrame)
	price_column_frame.pack(side = LEFT)
	priceLabel = Label(price_column_frame, text = "Price (£)")
	priceLabel.pack(side = TOP)

	quantity_column_frame = Frame(tableFrame)
	quantity_column_frame.pack(side = LEFT)
	quantityLabel = Label(quantity_column_frame, text = "Stock Level")
	quantityLabel.pack(side = TOP)

	# Then we populate the table with the *current* value of items
	update_stock(id_column_frame, name_column_frame, 
					price_column_frame, quantity_column_frame, items)

	# Then we populate the purchase frame
	# Note that while Rhys' StringVar solution did work for the button,
	# I was able to get it working properly by NOT STRINGING FUNCTIONS TOGETHER
	# (i.e. adding the grid at the end, do it on the next line instead)
	# This seems to be a common issue with tkinter so maybe avoid it alltogether!
	purchaseLabel = Label(purchaseFrame, text = "To Purchase: ")
	purchaseLabel.pack(side = LEFT)
	purchaseEntry = Entry(purchaseFrame)
	purchaseEntry.pack(side = LEFT)
	purchaseButton = Button(purchaseFrame, text = "Make Purchase",
							bg = "White", fg = "Blue",
							command = lambda: purchase(tableFrame, purchaseEntry.get(), items, totalSales)
							)
	purchaseButton.pack(side = RIGHT)

	# As this is not technically a new window, this is unnecessary
	# (technically as this is called from the login button we are still up on
	# line 37). However, for consistency and avoiding errors, there's nothing
	# wrong with including it anyway!
	# If this were a new window (see root at the bottom - this would absolutely
	# be necessary) 
	root.mainloop()



# This is the purchase function which handles whether a purchase can be made
# I don't like the fact we passes tableFrame into a method where it is largely
# irrelevant, so I will fix this in the decoupled-multiple-file program I make
def purchase(tableFrame, user_input, items, totalSales):

	try:
		key = int(user_input)

		if items[key]["Stock"] > 0:
			items[key]["Stock"] -= 1
			totalSales += items[key]["Price"]
			update_stock(tableFrame, items)
		else:
			messagebox.showwarning("Out of Stock!", "Out of Stock")

	except (ValueError, KeyError):
		messagebox.showwarning("Enter a Valid Key!", "Enter a Valid Key!")



# This is update stock function that populates the table based on our 
# items dictionary
# NOTE that we now have to pass through a frame for every column 
# just to keep our table structure!
def update_stock(id_column_frame, name_column_frame, 
					price_column_frame, quantity_column_frame, items):

	for i, item in enumerate(items):
		idLabel = Label(id_column_frame, text = item)
		idLabel.pack(side = BOTTOM)

		nameLabel = Label(name_column_frame, text = items[item]["Name"])
		nameLabel.pack(side = BOTTOM)

		priceLabel = Label(price_column_frame, text = items[item]["Price"])
		priceLabel.pack(side = BOTTOM)

		quantityLabel = Label(quantity_column_frame, text = items[item]["Stock"])
		quantityLabel.pack(side = BOTTOM)



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



# At the bottom of the file we define root (so that it is technically global)
# - in reality it is just in-scope of this entire .py file
# Note that root here is the actual window (or rather =Tk() creates a tkinter window)
# - for multiple windows we'd need multiple roots
root = Tk()

# We kick off our program by calling the login function
tk_login()
