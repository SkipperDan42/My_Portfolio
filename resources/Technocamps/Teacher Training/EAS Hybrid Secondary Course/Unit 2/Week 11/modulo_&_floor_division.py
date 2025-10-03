itemCost = 30.59
payment = 0
totalChange = 0
changePounds = 0
changePence = 0

print("Item costs £" + str(itemCost))

payment = float(input("How much are you paying in pounds? £"))

totalChange = payment - itemCost

changePounds = totalChange // 1
changePence = int(totalChange % 1 * 100)

print("Your change is %d pounds and %d pence" % (changePounds, changePence))

