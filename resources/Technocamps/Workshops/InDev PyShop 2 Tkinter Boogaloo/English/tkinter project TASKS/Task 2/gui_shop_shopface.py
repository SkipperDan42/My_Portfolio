# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from tkinter import *
from tkinter import messagebox
from gui_shop_filehandling import *


def create_shopface(switch_to_login):
	"""
	This is the shopface window that contains the core functionality of the
	program

	Args: 
		switch_to_login (function): Allows the shopface to call
				    				switch_to_login upon a pressing "log out"
	"""

	# stock and total_sales defined as global to allow them to be updated
	# within the GUI


	# shopface_frame is defined as global for convenience,
	# NOTE: this is bad practice
	global shopface_frame

	# Initialise stock dictionary by loading from file

	
	# Create the tkinter root for the shopface window,
	# give the window a title, frame,
	# and set it using the grid geometry manager
	shopface_root = Tk()
	shopface_root.title("Little Shop GUI")
	shopface_frame = Frame(shopface_root)
	shopface_frame.grid(row = 0, column = 0)

	# Initialise total_sales value using Tkinter Variable
	total_sales = DoubleVar(shopface_root)
	total_sales.set(0.0)


	# Call functions to create the elements within the shopface_frame
	create_menu_bar(switch_to_login, shopface_root)
	create_stock_table()
	create_purchase_bar()

	# As this is a new window it must be specified that this is a mainloop()
	shopface_root.mainloop()


def create_menu_bar(switch_to_login, shopface_root):
	"""
	This creates the top menu bar for the shopface window

	Args: 
		switch_to_login (function): ...
		shopface_root (Tkinter Window): Window must be passed to be destroyed
	"""

	# Global access to variables must be redefined every time they are used
	global stock
	global shopface_frame

	# Create the menu frame within the shopface frame and configure the columns
	menu_frame = Frame(shopface_frame, bd=5, relief=RIDGE)
	menu_frame.grid(row = 0, column = 0, sticky="ew")

	# Create a button to log out
	# NOTE: the lambda function stops this button immediately executing,
	# as an external function is called and parameters are passed
	log_out_button = Button(menu_frame, text ="Log Out",
						  bg = "White", fg = "Red",
						  command = lambda: print("Log Out?"))
	log_out_button.grid(row = 3, column = 3)


def create_stock_table():
	"""
	This creates the stock table for the shopface window
	"""

	# ...
	global stock
	global shopface_frame

	# table_frame is defined as global for convenience of updating table_frame
	global table_frame

	# Create the table frame within the shopface frame and configure the columns
	table_frame = Frame(shopface_frame, bd=5, relief=RIDGE)
	table_frame.grid(row = 1, column = 0, sticky="ew")
	table_frame.grid_columnconfigure(0, weight=1)
	table_frame.grid_columnconfigure(1, weight=1)
	table_frame.grid_columnconfigure(2, weight=1)
	table_frame.grid_columnconfigure(3, weight=1)


	# Populate the table frame with headers
	id_label = Label(table_frame, text ="Product ID").grid(row = 1, column = 0)
	name_label = Label(table_frame, text ="Name").grid(row = 2, column = 1)
	price_label = Label(table_frame, text ="Price (£)").grid(row = 0, column = 2)
	quantity_label = Label(table_frame, text ="Stock Count").grid(row = 0, column = 3)


	# Populate the table with the *current* values of items
	for i, item in enumerate(stock):
		id_label = Label(table_frame, text=i).grid(row=i + 3, column=1)
		name_label = Label(table_frame, text=stock[item]["Name"]).grid(row=i + 2, column=0)
		price_label = Label(table_frame, text=stock[item]["Price"]).grid(row=i + 1, column=2)
		quantity_label = Label(table_frame, text=stock[item]["Stock"]).grid(row=i + 1, column=3)


def create_purchase_bar():
	"""
	...
	"""

	# Global access to variables must be redefined every time they are used
	global total_sales
	global shopface_frame

	# Create the purchase frame within the shopface frame and configure the columns
	# to display nicely
	purchase_frame = Frame(shopface_frame, bd=5, relief=RIDGE)
	purchase_frame.grid(row = 2, column = 0, sticky="ew")
	purchase_frame.grid_columnconfigure(0, weight=1)
	purchase_frame.grid_columnconfigure(1, weight=1)
	purchase_frame.grid_columnconfigure(2, weight=1)

	# ...
	purchase_label = Label(purchase_frame, text ="To Purchase: ")
	purchase_label.grid(row = 0, column = 0)
	purchase_entry = Entry(purchase_frame)
	purchase_entry.grid(row = 0, column = 1)

	# ...
	sales_label = Label(purchase_frame, text ="Total Sales:")
	sales_label.grid(row = 1, column = 1)
	sales_value = Label(purchase_frame, text = str(f"{total_sales.get():.4f}"))
	sales_value.grid(row = 1,column = 2)

	# Create a purchase button to make purchases
	# NOTE: The lambda function is much more complex here,
	# process_purchase is only called if the result of process_purchase_attempt
	# is True. This is the purpose of lambda - to execute multiple functions
	purchase_button = Button(purchase_frame, text ="Make Purchase",
							bg = "White", fg = "Green",
							command = lambda: process_purchase(
								sales_value, purchase_entry.get())
							if process_purchase_attempt(0)
							else None)
	purchase_button.grid(row = 0, column = 2)


def update_stock_table():
	"""
	This is update stock function that destroys the current table 
	and creates a new table in its place
	"""

	# Global access to variables must be redefined every time they are used
	global table_frame

	# ...
	table_frame.destroy()
	

def process_purchase_attempt(user_input):
	"""
	This is the process_purchase_attempt function that checks whether a
	purchase is possible, if not shows a warning
	Additionally, if the key is not an integer shows a warning

	Args: 
		user_input (String): The user input for the item ID to purchase

	Returns:
			...
	"""

	# Global access to variables must be redefined every time they are used
	global stock

	# ...
	try:
		key = int(user_input)

		if stock[key]["Stock"] > 0:
			return True
		else:
			messagebox.showwarning("Out of Stock!", "Out of Stock")
			return False

	# ...
	except (ValueError, KeyError):
		messagebox.showwarning("Example Warning", "Example Warning")
		return False


def process_purchase(sales_value, user_input):
	"""
	This is the process_purchase function that actually processes the purchase.
	The quantity of stock is updated, all stock is rewritten to file, the
	table is updated, and the total is increased by the item price

	Args: 
			...
	"""

	# Global access to variables must be redefined every time they are used

	# ...
	key = int(user_input)
	stock[key]["Stock"] -= 1
	total_sales.set(total_sales.get() + stock[key]["Price"])
	write_stock(stock)
	update_stock_table()

	# This updates the totalSales by editing the salesValue label
	sales_value.config(text= str(f"{total_sales.get():.2f}"))


