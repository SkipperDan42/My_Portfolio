# Define all desired functions
def open_phonebook():
    phonebook = {}
    phonebook_file = open(desired_phonebook, "r")
    for contact in phonebook_file:
        contact = contact.replace("\n","").split(";")
        phonebook[contact[0]] = contact[1]
    return phonebook
    phonebook_file.close()

def update_phonebook():
    phonebook_file = open(desired_phonebook, "w")
    for contact in phonebook:
        phonebook_file.write(contact + ";" + phonebook[contact] + "\n")
    phonebook_file.close()

def add_contact(name, number):
    phonebook[name] = number
    print(f"Added {name}: {number}")

def get_contact(name):
    return phonebook.get(name, "Contact not found")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Deleted {name}")
    else:
        print("Contact not found")



# Define the phonebook location and dictionary
desired_phonebook = "phonebook.csv"
phonebook = {}


# Call the functions
phonebook = open_phonebook()
add_contact("Alice", "01792 424242")
add_contact("Bob", "01639 272727")
add_contact("Charles", "029 1212 3434")
print(get_contact("Alice"))
#delete_contact("Bob")
print(get_contact("Bob"))
update_phonebook()