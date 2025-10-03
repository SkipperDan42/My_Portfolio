#Task 5 demonstrates how to read in larger files in more advanced formats

def task():
    theUFOFile = open("UFO_Sightings.csv", "r")
    allUFOData = []

    for i, line in enumerate(theUFOFile):

        if i != 0:
            allUFOData.append(line.split(","))

    return allUFOData
