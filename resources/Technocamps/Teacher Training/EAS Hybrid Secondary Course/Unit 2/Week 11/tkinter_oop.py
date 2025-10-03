################################################################
# This is the full implementation of tkinter using OOP methods #
#                                                              #
# This is just for curiosity and A-Level knowledge             #
#                                                              #
# Hopefully you can see how despite having to repeat "self"    #
# this has simplified our lambda functions AS WELL AS making   #
# it simple to update total_sales, as these values now "belong"#
# to the Application class, and no longer need to be passed!   #
################################################################

import tkinter as tk
from tkinter import messagebox

# We make a new class that defines all behavours for our tkinter program
# Notice how EVERYTHING is now preceded by "self.", as they all belong to
# the current instance of this class (created at the bottom)
class Application:

    # We initialise the class when it is created to:
    # - have an instance variable called root (which is passed to the class)
    # - have an instance variable called total_sales
    # - have an instance variable called items (which is immediately loaded)
    # - call the login screen
    def __init__(self, root):
        self.root = root
        self.root.title("Shop Login")
        self.total_sales = 0
        self.items = self.load_stock()
        self.show_login_screen()


    #This method (function in a class) runs the login screen.
    def show_login_screen(self):

        # We create our login frame from the instance of root,
        # and define it to use the grid manager
        self.login_frame = tk.Frame(self.root)
        self.login_frame.grid(row=0, column=0)

        # We create a nice title at the top of our window
        tk.Label(self.login_frame, text="Welcome to here!").grid(
                                            row=0, column=0, columnspan=2)

        # We create the username label and text-entry fields
        tk.Label(self.login_frame, text="Username").grid(row=1, column=0)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=1, column=1)

        # We create the password label and text-entry fields
        # NOTE the show="*" keeps the password hidden!
        tk.Label(self.login_frame, text="Password").grid(row=2, column=0)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=2, column=1)

        # We create a button that calls the login function...
        # This is it! No clever work arounds, no lambda functions,
        # no passing parameters! Everything "belongs" to the application
        # SO. IT. JUST. DOES IT!
        tk.Button(
            self.login_frame, text="Submit", bg="White", fg="Red",
            command=self.login
        ).grid(row=3, column=1)


    # This function handles the actual login check
    # It calls the main window function if successful,
    # or throws an error message
    # NOTE that as the login window is not destroyed until the main window
    # function is run, then this can be run repeatedly!
    def login(self):

        stored_username = "dan"
        stored_password = "pass"

        if (self.username_entry.get() == stored_username and
                self.password_entry.get() == stored_password):
            self.show_main_screen()
        else:
            messagebox.showwarning("Failed!", "Login Failed!")


    # This is the main tkinter program, 
    # displaying the shop after a successful login.
    def show_main_screen(self):

        # No need to pass the login frame as it "belongs" to the application,
        # so we can just destory it here
        self.login_frame.destroy()

        # We create the new frame (whose parent is root),
        # and additionally the sub-frames (whose parent is the new frame)
        # that will hold the table and purchase information
        self.main_frame = tk.Frame(self.root)
        self.main_frame.grid(row=0, column=0)

        self.table_frame = tk.Frame(self.main_frame)
        self.table_frame.grid(row=1, column=0)

        self.purchase_frame = tk.Frame(self.main_frame)
        self.purchase_frame.grid(row=2, column=0)


        # We populate the table frame with headers
        # NOTE just a slightly more efficient method with a loop
        headers = ["Product ID", "Name", "Price (£)", "Stock Level"]
        for i, header in enumerate(headers):
            tk.Label(self.table_frame, text=header).grid(row=0, column=i)

        # Then we populate the table with the *current* value of items
        self.update_stock()

        # Then we populate the purchase frame
        tk.Label(self.purchase_frame, text="To Purchase: ").grid(row=0, column=0)
        self.purchase_entry = tk.Entry(self.purchase_frame)
        self.purchase_entry.grid(row=0, column=1)

        # We create a button that calls the purchase function...
        # Again, that's just it. No passing parameters, 
        # no stressing about how we keep totalSales up to date. SIMPLES.
        tk.Button(
            self.purchase_frame, text="Make Purchase", bg="White", fg="Blue",
            command=self.purchase
        ).grid(row=0, column=2)

    
    # This is the function which handles whether a purchase can be made
    # It's the same as before, just with a lot of "self"
    def purchase(self):
        try:
            key = int(self.purchase_entry.get())

            if self.items[key]["Stock"] > 0:
                self.items[key]["Stock"] -= 1
                self.total_sales += self.items[key]["Price"]
                self.update_stock()
            else:
                messagebox.showwarning("Out of Stock!", "Item is out of stock!")

        except (ValueError, KeyError):
            messagebox.showwarning("Invalid Input", "Enter a valid product ID!")

    
    # This is update stock function that populates the table based on our 
    # items dictionary.
    # Almost the same as before, 
    # but price uses an f-string to keep it a 2 decimal places
    def update_stock(self):
        for i, (item_id, item) in enumerate(self.items.items(), start=1):
            tk.Label(self.table_frame, text=item_id).grid(row=i, column=0)
            tk.Label(self.table_frame, text=item["Name"]).grid(
                                                            row=i, column=1)
            tk.Label(self.table_frame, text=f"£{item['Price']:.2f}").grid(
                                                            row=i, column=2)
            tk.Label(self.table_frame, text=item["Stock"]).grid(
                                                            row=i, column=3)


    # This is the load stock function that is currenty hardcoded
    # NOTE it is labeled as a static method as it never changes,
    # if there were 2 instances of Application this would be identical
    @staticmethod
    def load_stock():
        return {
            1: {"Name": "Ben Shaw's D&B", "Price": 1.20, "Stock": 20},
            2: {"Name": "Coca Cola", "Price": 1.50, "Stock": 100},
            3: {"Name": "Irn Bru", "Price": 0.99, "Stock": 32},
            4: {"Name": "R. White's Lemonade", "Price": 1.20, "Stock": 57}
        }


# When dealing with classes this just ensures that we are running the
# main program. Don't worry about this.
if __name__ == "__main__":

    # We define root so that it is in-scope of this entire .py file
    root = tk.Tk()

    # We create an instance of our Application class and 
    # provide it with a copy of root
    app = Application(root)

    # We call the main loop here, as root is also outside of the 
    # Application class.
    # This essentially means that our entire Application class is on 
    # the mainloop and will continue to run.
    root.mainloop()

