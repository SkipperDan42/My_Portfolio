# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os


def get_stock_file(mode):
	"""
	Opens the stock file from whatever directory is being used
	Is able to open the stock file in any mode (i.e. read/write)

	Args: mode (String): the mode in which to open the stock file

	Return: stock_file (File): returns the opened file in the desired mode
	"""

	directory = os.path.dirname(os.path.abspath(__file__))
	stock_path = os.path.join(directory,'sample_file.csv')
	stock_file = open(os.path.abspath(stock_path), mode)

	return stock_file


def load_stock():
	"""
	Load stock from file

	Return: stock (Dictionary): returns a dictionary containing all stock
	"""

	stock_file = get_stock_file('r')
	stock = {}

	for line in stock_file:
		
		item=[]
		for col in line.strip().split(','):
			item.append(col)

		item_id = int(item[0].strip())
		name = item[1].strip().replace('"','')
		price = int(item[2].strip())
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
	Write stock to file

	Args: stock (Dictionary): the dictionary to be written to file
	"""

	stock_file = get_stock_file('r')

	for item_id, item in stock.items():
		line =  str(str(item_id) + ', "' + item["Name"] + '", ' +
	    		str(item["Price"]) + ', ' + str(item["Stock"]) + '\n')
		stock_file.write(line)

	stock_file.close()