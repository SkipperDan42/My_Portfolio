import pandas as pd

# Task 5 - Read in a new csv file using the headers
# Use a list and a for loop to check how many Measures exist
# Sort these measures into alphabetical order
def task():
    allSeaLevels = pd.read_csv('Change in Mean Sea Levels.csv', usecols=['Measure', 'Date', 'Value'])
    #print(allSeaLevels)

    allMeasures = []
    for i in range(len(allSeaLevels)):
        if allSeaLevels.iloc[i,0] not in allMeasures:
            allMeasures.append(allSeaLevels.iloc[i,0])
    #print(allMeasures)

    allMeasures.sort()
    #print(allMeasures)

    return allSeaLevels, allMeasures