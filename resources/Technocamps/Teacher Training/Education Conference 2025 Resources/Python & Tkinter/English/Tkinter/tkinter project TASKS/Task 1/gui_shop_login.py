# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from tkinter import *
from tkinter import messagebox


def create_login():
	"""
	This will create the login window that will allow access into the shop

	Args: ...
	
	"""

	def pointless_function():
		"""
		This function is completely and utterly pointless.
		It's only real use will be to demonstrate why we'll be passing
		functions as variables.
		"""

		print("This functions is pointless.")


	def process_login():
		"""
		This function ...
		"""

		# Check the stored credentials against those entered into the fields
		stored_username = ""
		stored_password = ""

		if ((username_entry.get() == stored_username) or
				(password_entry.get() == stored_password)):

			# Launch the shopface program for a successful login
			print("Go Go Shopface!")

		else:
			# ...
			messagebox.showwarning("Failed!", "Failed!")


	# Create the tkinter root for the login window,
	# and give the window a title and a frame,
	# and pack them in with the geometry manager
	login_root = Tk()
	login_root.title("01")
	login_frame = Frame(login_root)
	login_frame.pack()


	# Create a title at the top of the login frame and pack it
	title_label = Label(login_frame, text = "Welcome to Shop Login!")


	# Create the username sub-frame, with label and text-entry fields
	username_frame = Frame(login_frame)
	username_frame.pack()
	username_label = Label(username_frame, text = "username")
	username_label.pack(side = LEFT)
	username_entry = Entry(username_frame)
	username_entry.pack(side = RIGHT)

	# ...
	password_frame = Frame(login_frame)
	password_frame.pack()
	password_label = Label(password_frame, text = "password")
	password_label.pack(side=RIGHT)
	password_entry = Entry(password_frame)
	password_entry.pack(side=LEFT)


	# Create a button that calls process_login when pressed
	submit_button = Button(login_frame, text = "submit",
							bg = "White", fg = "Red",
							command = pointless_method)
	submit_button.pack()

	# The mainloop function keeps this GUI active and waiting for user input
	# - this is essential code at the end of every new window
	login_root.mainloop()