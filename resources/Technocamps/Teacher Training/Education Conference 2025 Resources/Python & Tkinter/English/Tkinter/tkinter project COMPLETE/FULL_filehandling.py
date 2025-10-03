#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the filehandling module of the FULL Tkinter Shop Program. This module
implements the external file reading and writing capabilities. Run this module
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

import os

def get_stock_file(mode):
	"""
	This is the function to return the stock file from the directory. This
	function should work even after moving the directory (so long as the
	structure inside the directory is constant).

	Args:
		mode (String): The mode to open the stock file (e.g. read/write)

	Return: 
		stock_file (File): returns the opened file in the desired mode
	"""

	directory = os.path.dirname(os.path.abspath(__file__))
	stock_path = os.path.join(directory,'FULL_items.csv')
	stock_file = open(os.path.abspath(stock_path), mode)

	return stock_file


def load_stock():
	""" 
	This is the function to load stock from a file 

	Return: 
		stock (Dict): Dictionary containing all items in stock
	"""

	stock_file = get_stock_file('r')
	stock = {}

	for line in stock_file:
		
		item=[]
		for col in line.strip().split(','):
			item.append(col)

		item_id = int(item[0].strip())
		name = item[1].strip().replace('"','')
		price = float(item[2].strip())
		quantity = int(item[3].strip())
		stock[item_id] = {
						"Name": name,
						"Price": price,
						"Stock": quantity
						}
	stock_file.close()

	return stock


def write_stock(stock):
	""" 
	This is the function to write stock to a file 

	Args: 
		stock (Dict): Dictionary containing all items in stock
	"""

	stock_file = get_stock_file('w')

	for item_id, item in stock.items():
		line =  str(str(item_id) + ', "' + item["Name"] + '", ' +
	    		str(item["Price"]) + ', ' + str(item["Stock"]) + '\n')
		stock_file.write(line)

	stock_file.close()

