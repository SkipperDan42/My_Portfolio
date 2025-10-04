import pandas as pd

# Task 6
def task(allSeaLevels, allMeasures):
    seaLevelsByMeasure = {}
    for measure in allMeasures:
        seaLevelsByMeasure[measure] = allSeaLevels.loc[allSeaLevels['Measure'] == measure, ['Date','Value']]
    #print(seaLevelsByMeasure)

    # print(seaLevelsByMeasure["Baltic Sea"].get['Date'])

    return seaLevelsByMeasure