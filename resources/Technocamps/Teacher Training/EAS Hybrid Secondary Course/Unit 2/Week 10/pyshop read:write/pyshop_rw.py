################################################################
# This is the full implementation we were doing in the session #
################################################################

from tkinter import *
from tkinter import messagebox



# This is the tkinter login screen GUI
def tk_login():

	# We create our login frame from the root window,
	# and define it to use the grid manager
	loginFrame = Frame(root)
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
							command = lambda: tk_main(loginFrame) 
							if login(usernameEntry.get(), passwordEntry.get()) 
							else messagebox.showwarning("Failed!", "Failed!"))
	submitButton.grid(row = 3, column = 1)

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

	# Then we populate the table with the *current* value of items
	update_stock(tableFrame, items)

	# Then we populate the purchase frame
	# Note that while Rhys' StringVar solution did work for the button,
	# I was able to get it working properly by NOT STRINGING FUNCTIONS TOGETHER
	# (i.e. adding the grid at the end, do it on the next line instead)
	# This seems to be a common issue with tkinter so maybe avoid it alltogether!
	purchaseLabel = Label(purchaseFrame, text = "To Purchase: ")
	purchaseLabel.grid(row = 0, column = 0)
	purchaseEntry = Entry(purchaseFrame)
	purchaseEntry.grid(row = 0, column = 1)
	purchaseButton = Button(purchaseFrame, text = "Make Purchase",
							bg = "White", fg = "Blue",
							command = lambda: purchase(tableFrame, purchaseEntry.get(), items, totalSales)
							)
	purchaseButton.grid(row = 0, column = 2)


        #defining a button to save stock information to file before we close the program
	#calls the store_stock() function when clicked and passes the items dictionary
	saveButton = Button(purchaseFrame, text = "Save",
                            bg = "White", fg = "Blue",
                            command = lambda: store_stock(items)
                            )
	saveButton.grid(row = 0, column = 3)
	

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
		key = user_input

		if items[key]["Stock"] > 0:
			items[key]["Stock"] -= 1
			totalSales += items[key]["Price"]
			update_stock(tableFrame, items)
		else:
			messagebox.showwarning("Out of Stock!", "Out of Stock")

	except (ValueError, KeyError):
		messagebox.showwarning("Enter a Valid Key!", "Enter a Valid Key!")



# This is update stock function that populates the table based on our items dictionary
def update_stock(tableFrame, items):

	for i, item in enumerate(items):
		idLabel = Label(tableFrame, text = item).grid(row = i + 1, column = 0)
		nameLabel = Label(tableFrame, text = items[item]["Name"]).grid(row = i + 1, column = 1)
		priceLabel = Label(tableFrame, text = items[item]["Price"]).grid(row = i + 1, column = 2)
		quantityLabel = Label(tableFrame, text = items[item]["Stock"]).grid(row = i + 1, column = 3)



# This is the load stock function to load from file
def load_stock():
        # we load the file as a read file
        stockData = open('Stock.csv', 'r')
        items = {}

        #for each row in our file we pull out the data into a list
        #then set a key in our dictionary to point to that information
        for row in stockData:
                item = []

                for column in row.strip().split(','):
                        item.append(column)
                
                items[item[0]] = {"Name":item[1],
                                  "Price":int(item[2]),
                                  "Stock":int(item[3])}
                
        #finally we close the file and return the dictionary
        stockData.close()
        return items


#this is the store stock function to save to file
#we pass a dictionary containing our shop items
def store_stock(items):
        # we load the file as a write file
        stockData = open('Stock.csv', 'w')

        # for each key in our dictionary we turn that data into a suitable csv string
        #then write that string as a line in our file
        for row in range(len(items)):
                key = str(row + 1)

                text = key + "," + items[key]["Name"] + "," + str(items[key]["Price"]) + "," + str(items[key]["Stock"]) + "\n"

                stockData.write(text)

        #finally we close the file
        stockData.close()



# At the bottom of the file we define root (so that it is technically global)
# - in reality it is just in-scope of this entire .py file
# Note that root here is the actual window (or rather =Tk() creates a tkinter window)
# - for multiple windows we'd need multiple roots
root = Tk()

# We kick off our program by calling the login function
tk_login()
