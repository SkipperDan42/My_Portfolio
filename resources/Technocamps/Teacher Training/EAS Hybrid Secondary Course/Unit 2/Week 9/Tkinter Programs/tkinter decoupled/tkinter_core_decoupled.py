from tkinter import *
from tkinter import messagebox
from tkinter_filehandling_decoupled import *


# This is the core tkinter program, displaying the shop
# (avoiding calling it main - as main just launches everything)
def tk_core():

	# And here is the main window,
	# created independently of the login window!
	main_root = Tk()

	# We initialise our shop variables when opening the main program
	items = load_stock()
	totalSales = 0

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

	# Then we populate the purchase frame (but not the button - yet)
	purchaseLabel = Label(purchaseFrame, text = "To Purchase: ")
	purchaseLabel.grid(row = 0, column = 0)
	purchaseEntry = Entry(purchaseFrame)
	purchaseEntry.grid(row = 0, column = 1)

	# Now we populate the purchase frame with the sales info!
	# This is so that we can pass the salesValue to the update function
	salesLabel = Label(purchaseFrame, text = "Total Sales:")
	salesLabel.grid(row = 1, column = 1)
	salesValue = Label(purchaseFrame, text = str(f"{totalSales:.2f}"))
	salesValue.grid(row = 1,column = 2)

	# Then we populate the table with the *current* value of items
	# NOTE that we're doing this later so we can pass salesValue
	update(tableFrame, salesValue, items, totalSales)

	# Our lambda function is much more complex here, and makes use of
	# two separate purchase methods - this is explained below!
	purchaseButton = Button(purchaseFrame, text = "Make Purchase",
							bg = "White", fg = "Blue",
							command = lambda: make_purchase(tableFrame, salesValue, 
											purchaseEntry.get(), items, totalSales)
							if attempt_purchase(purchaseEntry.get(), items)
							else messagebox.showwarning("Out of Stock!", "Out of Stock")
							)
	purchaseButton.grid(row = 0, column = 2)

	# As this is a new window we need to specify that this is a mainloop()
	main_root.mainloop()



# This purchase function simply checks whether a purchase is possible
# it either returns True/False or throws/catches an error
# This allows us to use an if in our lambda function (MORE BELOW!)
def attempt_purchase(user_input, items):

	try:
		key = int(user_input)

		if items[key]["Stock"] > 0:
			return True
		else:
			return False

	except (ValueError, KeyError):
		messagebox.showwarning("Enter a Valid Key!", "Enter a Valid Key!")



# This purchase function actually handles the purchase and calls update!
#
# OKAY - so basically, lambda functions don't truly return the values when
# called. So when we changed the value of totalSales it wouldn't update as
# it hadn't changed in tk_core() [or rather tk_main() in your versions]
#
# HOWEVER - by changing our lambda function to run this IF the other function
# is true, suddenly we can return the values (as they are and always were 
# in scope).
#
# DON'T worry too much about this, this is way out of scope of GCSE and
# honestly is EXACTLY why you use Object Oriented for this sort of thing.
# It is genuinely far easier to use global variables in these situatuations!
def make_purchase(tableFrame, salesValue, user_input, items, totalSales):

	key = int(user_input)
	items[key]["Stock"] -= 1
	totalSales += items[key]["Price"]
	update(tableFrame, salesValue, items, totalSales)



# This is update stock function that populates the table based on our items dictionary
# It also resets the salesValue Label
def update(tableFrame, salesValue, items, totalSales):

	for i, item in enumerate(items):
		idLabel = Label(tableFrame, text = item).grid(row = i + 1, column = 0)
		nameLabel = Label(tableFrame, text = items[item]["Name"]).grid(row = i + 1, column = 1)
		priceLabel = Label(tableFrame, text = items[item]["Price"]).grid(row = i + 1, column = 2)
		quantityLabel = Label(tableFrame, text = items[item]["Stock"]).grid(row = i + 1, column = 3)

	# This updates the totalSales by editing the salesValue label
	salesValue.config(text = str(f"{totalSales:.2f}"))
