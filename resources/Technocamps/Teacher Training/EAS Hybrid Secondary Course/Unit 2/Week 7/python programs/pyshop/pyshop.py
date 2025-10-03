#defining login function
def login():
    #sets correct username and password
    username = "alex123"
    password = "guest"

    #takes user input for login attempt
    inpUsername = input("Enter your username: ")
    inpPassword = input("enter your password: ")

    #compares the user input login credentials to the correct credentials
    #if matching, a welcome message is shown and the menu function is called
    #otherwise the user is informed of their error and the login is restarted
    if inpUsername == username and inpPassword == password:
        print("Welcome!")
        menu()
    else:
        print("Username or Password incorrect")
        login()


#defining menu function
def menu():
    #displays list of commands to the user
    print("Select one of the following: \n1.View Items\n2.Purchase\n3.View Sales")

    #try/except pair handles user input error
    try:
        #takes user input for chosen command
        selection = int(input("Enter the corresponding number: "))

        #performs appropriate actions for 1, 2 or 3
        if selection == 1:
            print("You have selected 'View Items'")

            #iterates through the item dictionary
            #prints information about each item on a new line
            for item in items:
                print(items[item])
                menu()
                
        elif selection == 2:
            print("You have selected 'Purchase'")
            purchase()
                
        elif selection == 3:
            print("You have selected 'View Sales'")
            view_sales()

        #if user enters an integer other than 1, 2 or 3
        #prints an error message, then restarts the menu
        else:
            print("Invalid selection - only enter 1, 2 or 3")
            menu()

    #if the user does not input an integer
    #prints an error message, then restarts the menu
    except ValueError:
        print("Please only enter an integer for your selection")
        menu()


#function allowing a user to purchase an item
def purchase():
    item = input("Please enter an item key value to purchase") #gets item key as input from user

    #try/except pair handle error if user does not enter a valid key
    try:
        key = int(item) #converts user input to integer
        
        print("You have bought", items[key]["name"]) #informs the user the purchase was successful

        #adds the cost of the purchased item to the global variable totalSales
        global totalSales
        totalSales += items[key]["price"]

        #reduces stock of purchased item by 1
        items[key]["numStock"] = items[key]["numStock"] - 1

        #returns to the menu
        menu()

    #if key invalid:
    #informs the user and restarts the purchase
    except ValueError:
        print("Please enter a valid key")
        purchase()


#function to view total sales made
def view_sales():
    print(totalSales)
    menu()


#main code
#global variable to track total sales made
totalSales = 0
            
#dictionary defining shop items
#each item is its own dictionary within the main dictionary
items = {
    1: {
        "name": "Dairy Milk Plain Chocolate",
        "price": 80,
        "numStock": 15
        },
    
    2: {
        "name": "Lucozade Sport",
        "price": 180,
        "numStock": 10
        },
    
    3: {
        "name": "Strawberry Laces",
        "price": 30,
        "numStock": 8
        }
    }

#calling the login function
login()
