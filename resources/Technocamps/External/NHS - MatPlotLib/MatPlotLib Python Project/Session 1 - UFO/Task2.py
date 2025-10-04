#Task 2 is to understand how to edit data as it is read from a file

def task():
    dietSource = open("DansDiet.txt", "r")
    diet = []

    for line in dietSource:
        diet.append(line.replace("\n", ""))

    print(diet)

    dietItems = []
    dietCounts = []

    for item in diet:
        if item in dietItems:
            for entry in dietCounts:
                if entry[0] == item:
                    entry[1] += 1
        else:
            dietItems.append(item)
            dietCounts.append([item, 1])


    return dietCounts