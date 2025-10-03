#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the login module of the FULL Tkinter Shop Program. This module
implements the login logic and runs the login window. Run this module to run
the program.

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


def create_login(switch_to_shop):
	"""
	This is the login window to allow access into the shop

	Args: 
		switch_to_shopface (function): Allows the login to call
									   switch_to_shopface upon a successful
									   login
	"""

	
	def process_login():
		"""
		This function handles the actual login and validation, after pressing
		the button. If the login was successful then we call switch_to_shop to
		delete this window and call the shopface program

		NOTE: It is weird to see functions within functions, and is usually
		redundant, though you may see it occasionally. In this case, it will
		stop our button from running automatically on start-up.
		"""

		# Store the login credentials
		stored_username = "dan"
		stored_password = "pass"

		# Check whether the login credentials match the user input
		if ((username_entry.get() == stored_username) and
				(password_entry.get() == stored_password)):

			# Now we call switch_to_shop to launch the shopface program
			switch_to_shop(login_root)

		else:
			messagebox.showwarning("Failed!", "Failed!")


	# Create the tkinter root for the login window,
	# give the window a title, create a login frame within,
	# and pack it using the pack geometry manager
	login_root = Tk()
	login_root.title("Little Shop Login")
	login_frame = Frame(login_root)
	login_frame.pack()

	# Within the login_frame,
	# create a title at the top of the frame and pack it
	title_label = Label(login_frame, text = "Welcome to Shop Login!")
	title_label.pack()

	# Within the login_frame,
	# create the username frame, label and text-entry fields
	# pack them all
	username_frame = Frame(login_frame)
	username_frame.pack()
	username_label = Label(username_frame, text = "username")
	username_label.pack(side = LEFT)
	username_entry = Entry(username_frame)
	username_entry.pack(side = RIGHT)

	# Within the login_frame,
	# create the password frame, label and text-entry fields
	# pack them all
	password_frame = Frame(login_frame)
	password_frame.pack()
	password_label = Label(password_frame, text = "password")
	password_label.pack(side=LEFT)
	password_entry = Entry(password_frame)
	password_entry.pack(side=RIGHT)

	# Within the login_frame,
	# create a button that calls process_login,
	# pack it
	submit_button = Button(login_frame, text = "submit",
							bg = "White", fg = "Red",
							command = process_login)
	submit_button.pack()

	# The mainloop function keeps this GUI in a loop (i.e. keeps it active)
	# and waiting for user input - we need this at the end of every new window
	login_root.mainloop()