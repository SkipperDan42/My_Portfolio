#SOLUTION 1 - Nested If
#takes user input for their name and age
#age is cast to an integer so it can be compared to other numbers
name = input("What is your name? ")
age = int(input("What is your age?" ))

#if age is 17 or  greater
#will take user input for whether they have passed their test
#user input is immediately cast to a boolean for comparison
if age >= 17:
    passed = bool(input("Have you passed your test? True/False : ")

    #prints appropriate message based upon user input
    if passed:
        print(name, "is old enough to drive and has passed")
    else:
        print("Pass your test!")

#if age < 17
#displays appropriate message
#avoids asking user if they have passed their test if they are too young
else:
    print(name + (" is not old enough to drive"))


#SOLUTION 2 - Elif Statements
#takes user input as in solution 1
#also takes input for passing driving test at the start
name = input("What is your name? ")
age = int(input("What is your age?" ))
passedStr = input("Have you passed your test? y/n : ")

#alternative method of setting a boolean based on user input
#uses a seperate 'passedBool' variable
#passedBool is set based upon user input
#this method avoids crashes if the user input is invalid
passedBool = False
if passedStr == 'y':
    passedBool = True

#an appropriate message is displayed based upon the user input
if age >= 17 and passedBool:
    print(name, "is old enough to drive and has passed")
elif age >= 17 and not passedBool:
    print("Pass your test!")
else:
    print(name, "is not old enough to drive")
