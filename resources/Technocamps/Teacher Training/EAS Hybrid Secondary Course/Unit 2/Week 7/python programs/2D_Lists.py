#2D List - a list of lists
#this menu variable contains a list of 3 lists
menu = [["starter1", "starter2", "starter3"],
        ["main1", "main2", "main3", "main4"],
        ["dessert1", "dessert2", "dessert3", "dessert4", "dessert5"]]

#print the whole menu list
print(menu)

#removes 'starter1' from the 1st list (starters) in the larger menu list
menu[0].remove("starter1")

#appends "new dessert" to the 3rd list (desserts) in the larger menu list
menu[2].append("new dessert")

#prints the 3rd element of the 2nd list ("main3")
print(menu[1][2])

#prints the entire 3rd list (desserts)
print(menu[2])

#prints the length of the menu list
print(len(menu))

#prints the length of the 1st list in the larger list
print(len(menu[0]))
