#Task 1 is to understand how to read in a file from data

def task():
    dietSource = open("DansDiet.txt", "r")
    diet = []

    for line in dietSource:
        diet.append(line)

    print(diet)


