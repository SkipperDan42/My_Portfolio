import matplotlib.pyplot as plt

# Task 2 is to teach basic pandas operations
def task(athleteData):

    #This is how we can filter a DataFrame to include only specific results
    goldAthletes = athleteData[athleteData["Medal"] == "Gold"]
    print(goldAthletes)


    #This is how we can get the mean result of a column
    meanAge = athleteData["Age"].mean()
    print(meanAge.round())


    #Using multiple conditions and printing the number of results in each
    medalBelowMean = athleteData[(athleteData["Medal"].notna()) & (athleteData["Age"] < 26)]
    medalAboveMean = athleteData[(athleteData["Medal"].notna()) & (athleteData["Age"] >= 26)]
    print(f"Below Average Age: {len(medalBelowMean)}\nAbove Average Age: {len(medalAboveMean)}")


    #Getting the oldest and youngest athletes
    athleteAgeSort = athleteData[athleteData["Age"].notna()].sort_values("Age",ascending=False)
    print(athleteAgeSort.head())
    print(athleteAgeSort.tail())