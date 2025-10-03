#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the add_stock module of the FULL Tkinter Shop Program. This module
implements the window to add new items of stock to the shop. Run this module
to run the program.

This program was intended as an exercise for the WJEC 2025 Computing curriculum
(specifically the new exam style for Unit 2).

The aim of the task is to understand the program and fix all the errors that
are present, while improving the learners' ability to provide good comments and
documentation.

NOTE: This is a FULL version of the program without any errors, to be used by
      the teacher to support the learners! 
      The documentation in this program is not a WJEC GCSE requirement, but it
      is included for completeness. Some of the comments are too descriptive, 
      but are included to be helpful.
"""
__author__ = "Dan North"
__maintainer__ = "Technocamps"
__date__ = "2025/08/27"
__deprecated__ = False

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from tkinter import *
from tkinter import messagebox
from FULL_shopface import *
from FULL_filehandling import write_stock


def create_add_stock(update_stock_table, stock):
	"""
	This is the function to create the add stock window
	
	Args: 
		update_stock_table (Function): The function to update the stock table
									   in the shopface window
		stock (Dict): The dictionary of all items for sale
	"""

	# Create the tkinter root for the add stock window,
	# give the window a title,
	# create an add stock frame from the root,
	# and set it to the grid using the grid geometry manager
	add_root = Tk()
	add_root.title("Little Shop Add Stock")
	add_frame = Frame(add_root)
	add_frame.grid(row = 0, column = 0)

	# Create a nice title at the top of the window,
	# Set it in place with the grid manager,
	# and configure the column so that it is centered
	title_label = Label(add_frame, text = "Add a new item to the stock list:")
	title_label.grid(row = 0, column = 0, sticky="ew")
	title_label.grid_columnconfigure(0, weight=1)

	# Create a label and entry field for the item ID,
	# Set them in place with the grid manager
	id_label = Label(add_frame, text = "Item ID")
	id_label.grid(row = 1, column = 0)
	id_entry = Entry(add_frame)
	id_entry.grid(row = 1, column = 1)

	# Create a label and entry field for the item Name,
	# Set them in place with the grid manager
	name_label = Label(add_frame, text = "Name")
	name_label.grid(row = 2, column = 0)
	name_entry = Entry(add_frame)
	name_entry.grid(row = 2, column = 1)

	# Create a label and entry field for the item Price,
	# Set them in place with the grid manager
	price_label = Label(add_frame, text = "Price")
	price_label.grid(row = 3, column = 0)
	price_entry = Entry(add_frame)
	price_entry.grid(row = 3, column = 1)

	# Create a label and entry field for the item Quantity,
	# Set them in place with the grid manager
	quantity_label = Label(add_frame, text = "Quantity")
	quantity_label.grid(row = 4, column = 0)
	quantity_entry = Entry(add_frame)
	quantity_entry.grid(row = 4, column = 1)

	# Create a button to add the item to stock,
	# Using a lambda function so that process_add_item only runs when pressed
	add_button = Button(add_frame, text = "Add Item",
							bg = "White", fg = "Green",
							command = lambda: process_add_item(
												add_root, update_stock_table,
												stock, id_entry, name_entry,
												price_entry, quantity_entry))
	add_button.grid(row = 5, column = 1)

	# New window, so new mainloop!
	add_root.mainloop()


def validate_add(id_entry, name_entry, price_entry, quantity_entry):
	"""
	This function validates the contents of the user entry fields
	NOTE: If this is successful all return values will have their necessary
		  types, but if unsuccessful the failed return value will be False

	Args: 
		id_entry (String): The user entry for the new items ID
		name_entry (String): The user entry for the new items Name
		price_entry (String): The user entry for the new items Price
		quantity_entry (String): The user entry for the new items Quantity
	  
	Returns: 
		item_id (False / int): The return value items ID
		name (False / String): The return value items Name
		price (False / float): The return value items Price
		quantity (False / int): The return value items Quantity
	"""

	item_id, name, price, quantity = False, False, False, False

	if ((id_entry.get() == "") or (name_entry.get() == "") or
		(price_entry.get() == "") or (quantity_entry.get() == "")):
		messagebox.showwarning("Error", "All fields must have values!")
	else:
		try:
			item_id = int(id_entry.get())
		except ValueError:
			messagebox.showwarning("Error", "Item ID must be an integer!")
			return item_id, name, price, quantity

		try:
			price = float(price_entry.get())
		except ValueError:
			messagebox.showwarning("Error", "Price must be a number!")
			return item_id, name, price, quantity

		try:
			quantity = int(quantity_entry.get())
		except ValueError:
			messagebox.showwarning("Error", "Quantity must be an integer!")
			return item_id, name, price, quantity

		name = name_entry.get()

	return item_id, name, price, quantity


def process_add_item(add_root, update_stock_table, stock, id_entry,
					 name_entry, price_entry, quantity_entry):
	"""
	This is the process_add_item function that attempts to add an item if the
	user entry fields are successfully validated.
	The item is added to stock, the stock is rewritten to file, and the table
	is updated. Additionally the add stock window is destroyed

	Args: 
		add_root (Tkinter Window): The window to be destroyed
		update_stock_table (function): The function to update the shopface
									   table
		stock (dictionary): The dictionary of all items for sale
		id_entry (String): The user entry for the new items ID
		name_entry (String): The user entry for the new items Name
		price_entry (String): The user entry for the new items Price
		quantity_entry (String): The user entry for the new items Quantity
	"""

	item_id, name, price, quantity = validate_add(id_entry, name_entry,
												  price_entry, quantity_entry)

	if ((item_id != False) and (name != False) and 
		  (price != False) and (quantity != False)):

		stock[item_id] = {	"Name": name,
							"Price": price,
							"Stock": quantity
							}
		write_stock(stock)
		update_stock_table()
		add_root.destroy()
