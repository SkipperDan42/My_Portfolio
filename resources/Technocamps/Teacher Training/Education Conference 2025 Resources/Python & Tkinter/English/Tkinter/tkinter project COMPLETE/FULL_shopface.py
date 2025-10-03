#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the shopface module of the FULL Tkinter Shop Program. This module
implements the main shop window. Run this module to run the program.

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
from FULL_filehandling import *
from FULL_add_stock import *


def create_shopface(switch_to_login):
	"""
	This is the shopface window that contains the core functionality of the
	program

	Args: 
		switch_to_login (function): Allows the shopface to call
							 	    switch_to_login upon a pressing "log out"
	"""

	# stock and total_sales must be defined as global to allow them to be
	# updated within the GUI (other solutions exist but this is the simplest)
	global stock
	global total_sales

	# shopface_frame is defined as global for convenience,
	# NOTE: this is bad practice
	global shopface_frame

	# Initialise stock dictionary by loading from file
	stock = load_stock()

	# Create the tkinter root for the shopface window,
	# give the window a title,
	# create a shopface frame from the root,
	# and set it to the grid using the grid geometry manager
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

	# As this is a new window we need to specify that this is a mainloop()
	shopface_root.mainloop()


def create_menu_bar(switch_to_login, shopface_root):
	"""
	This creates the top menu bar for the shopface window

	Args: 
		switch_to_login (Function): Allows the shopface to call
							 		switch_to_login upon a pressing "log out"
		shopface_root (Tkinter Window): Window must be passed to be destroyed
	"""

	# Global access to variables must be redefined every time they are used
	global stock
	global shopface_frame

	# Create the menu frame within the shopface frame and configure the columns
	# to display nicely
	menu_frame = Frame(shopface_frame, bd=5, relief=RIDGE)
	menu_frame.grid(row = 0, column = 0, sticky="ew")
	menu_frame.grid_columnconfigure(0, weight=1)
	menu_frame.grid_columnconfigure(1, weight=1)
	menu_frame.grid_columnconfigure(2, weight=1)

	# Create a button to add stock in the menu frame,
	# This button will open the add window
	# NOTE: the lambda function stops this button immediately executing,
	# as an external function is called and parameters are passed
	add_button = Button(menu_frame, text ="Add Stock",
						bg = "White", fg = "Blue",
						command = lambda: create_add_stock(update_stock_table,
															stock))
	add_button.grid(row = 0, column = 0)

	# Create a button to log out in the menu frame,
	# This button will call switch_to_login to log out of the shopface
	# NOTE: the lambda function serves the same purpose
	log_out_button = Button(menu_frame, text ="Log Out",
						  bg = "White", fg = "Red",
						  command = lambda: switch_to_login(shopface_root))
	log_out_button.grid(row = 0, column = 2)


def create_stock_table():
	"""
	This creates the stock table for the shopface window
	"""

	# Global access to variables must be redefined every time they are used
	global stock
	global shopface_frame

	# table_frame is defined as global for convenience of updating table_frame
	# NOTE: this is bad practice
	global table_frame

	# Create the table frame within the shopface frame and configure the columns
	# to display nicely
	table_frame = Frame(shopface_frame, bd=5, relief=RIDGE)
	table_frame.grid(row = 1, column = 0, sticky="ew")
	table_frame.grid_columnconfigure(0, weight=1)
	table_frame.grid_columnconfigure(1, weight=1)
	table_frame.grid_columnconfigure(2, weight=1)
	table_frame.grid_columnconfigure(3, weight=1)


	# Populate the table frame with headers
	id_label = Label(table_frame, text ="Product ID").grid(row = 0, column = 0)
	name_label = Label(table_frame, text ="Name").grid(row = 0, column = 1)
	price_label = Label(table_frame, text ="Price (£)").grid(
														row = 0, column = 2)
	quantity_label = Label(table_frame, text ="Stock Level").grid(
														row = 0, column = 3)


	# Populate the table with the *current* values of items
	for i, item in enumerate(stock):
		id_label = Label(table_frame, text=item).grid(row=i + 1, column=0)
		name_label = Label(table_frame, text=stock[item]["Name"]).grid(
														row=i + 1, column=1)
		price_label = Label(table_frame, text=stock[item]["Price"]).grid(
														row=i + 1, column=2)
		quantity_label = Label(table_frame, text=stock[item]["Stock"]).grid(
														row=i + 1, column=3)


def create_purchase_bar():
	"""
	This creates the purchase bar for the shopface window
	"""

	# Global access to variables must be redefined every time they are used
	global total_sales
	global shopface_frame

	# Create the purchase frame within the shopface frame and configure the
	# columns to display nicely
	purchase_frame = Frame(shopface_frame, bd=5, relief=RIDGE)
	purchase_frame.grid(row = 2, column = 0, sticky="ew")
	purchase_frame.grid_columnconfigure(0, weight=1)
	purchase_frame.grid_columnconfigure(1, weight=1)
	purchase_frame.grid_columnconfigure(2, weight=1)

	# Populate the purchase frame with a purchase label and a user entry field
	purchase_label = Label(purchase_frame, text ="To Purchase: ")
	purchase_label.grid(row = 0, column = 0)
	purchase_entry = Entry(purchase_frame)
	purchase_entry.grid(row = 0, column = 1)

	# Populate the purchase frame with a sales label and sales value
	sales_label = Label(purchase_frame, text ="Total Sales:")
	sales_label.grid(row = 1, column = 1)

	# TODO: USE A TKINTER VARIABLE HERE FOR SALES VALUE

	sales_value = Label(purchase_frame, text = str(f"{total_sales.get():.2f}"))
	sales_value.grid(row = 1,column = 2)

	# Create a purchase button to make purchases
	# NOTE: The lambda function is much more complex here,
	# process_purchase is only called if the result of process_purchase_attempt
	# is True
	# This is the purpose of lambda functions, to execute multiple functions
	purchase_button = Button(purchase_frame, text ="Make Purchase",
							bg = "White", fg = "Green",
							command = lambda: process_purchase(sales_value, 
														purchase_entry.get())
							if process_purchase_attempt(purchase_entry.get())
							else None)
	purchase_button.grid(row = 0, column = 2)


def update_stock_table():
	"""
	This is update stock function that destroys the table_frame 
	and calls the create_stock_table function
	"""

	global table_frame
	table_frame.destroy()
	create_stock_table()
	

def process_purchase_attempt(user_input):
	"""
	This is the process_purchase_attempt function that checks whether a
	purchase is possible, if it is it returns True, if not shows a warning
	Additionally, if the key is not an integer shows a warning

	Args: 
		user_input (String): The user input for the item ID to purchase

	Returns:
		(boolean): True if attempt successful, if unsuccessful False
	"""

	global stock

	try:
		key = int(user_input)

		if stock[key]["Stock"] > 0:
			return True
		else:
			messagebox.showwarning("Out of Stock!", "Out of Stock")
			return False

	except (ValueError, KeyError):
		messagebox.showwarning("Enter a Valid Key!", "Enter a Valid Key!")
		return False


def process_purchase(sales_value, user_input):
	"""
	This is the process_purchase function that actually processes the purchase.
	The quantity in stock is updated, the stock is rewritten to file, the
	table is updated, and total_sales is increased by the item price

	Args: 
		sales_value (Tkinter Label): The label that displays total_sales
		user_input (String): The user input for the item ID to purchase 
	"""

	global stock
	global total_sales

	key = int(user_input)
	stock[key]["Stock"] -= 1
	total_sales.set(total_sales.get() + stock[key]["Price"])
	write_stock(stock)
	update_stock_table()

	# This updates the totalSales by editing the salesValue label
	sales_value.config(text= str(f"{total_sales.get():.2f}"))