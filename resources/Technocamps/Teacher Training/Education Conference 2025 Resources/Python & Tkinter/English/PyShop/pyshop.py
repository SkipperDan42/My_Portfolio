def main():

    login_successful = False
    while not login_successful:
        login_successful = login()

    load_items()
    
    in_menu = True
    while in_menu:
        menu()


def login():

    stored_username = "admin"
    stored_password = "pass"

    in_username = input("Enter username: ")
    in_password = input("Enter password: ")

    if (stored_username == in_username) and (stored_password == in_password):
        print("Welcome!")
        return True

    else:
        print("Login failed!")
        return False


def menu():

    menu_choice = input("""
    Please select an option:
    1. View
    2. Add
    3. Delete
    """)

    try:
        selection = int(menu_choice)
        if selection == 1:
            view_all()

        elif selection == 2:
            add_item()

        elif selection == 3:
            delete_item()

        else:
            print("Invalid selection!")

    except ValueError:
        print("Must enter a valid integer!")


def load_items():

    global items

    stock_file = open('stock.csv','r')
    items = []

    for line in stock_file:
        item = []

        for column in line.strip().split(','):
            item.append(column)

        items.append({
                        "Name":    item[0],
                        "Price":   int(item[1]),
                        "InStock": int(item[2])
                    })

    stock_file.close()



def save_items():

    global items

    stock_file = open('stock.csv','w')

    for item in items:
        line = item["Name"] + "," + str(item["Price"]) + "," +
                str(item["InStock"]) + "\n"

        stock_file.write(line)

    stock_file.close()


def view_all():

    global items

    for item in items:
        print("Name: " + item["Name"])
        print("Price: " + str(item["Price"]))
        print("Stock: " + str(item["InStock"]) + "\n")



def add_item():

    global items

    new_item = dict()
    new_item["Name"] = input("Item name: ")
    new_item["Price"] = float(input("Item price: "))
    new_item["InStock"] = int(input("Number in stock: "))
    
    items.append(new_item)
    save_items()


def delete_item():

    global items
    item_name = input("Name of item to delete: ")

    for item in items:
        if item["Name"] == item_name:

            print("Name: " + item["Name"])
            print("Price: " + str(item["Price"]))
            print("Stock: " + str(item["InStock"]) + "\n")

        confirm = input("Delete item? Y/N: ")
        if confirm == "Y":
            items.remove(item)
            save_items()
