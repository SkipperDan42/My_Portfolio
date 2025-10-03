password = "guest"
userInput = input("Enter Password: ")

while userInput != password:
    print("Password incorrect")
    userInput = input("Enter Password: ")

print("Password accepted")
