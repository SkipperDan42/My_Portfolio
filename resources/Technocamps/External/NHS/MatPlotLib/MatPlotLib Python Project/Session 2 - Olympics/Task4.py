import matplotlib.pyplot as plt

# Task 4 is plotting specific groups from the data.
def task(athleteData, countryCode):

    #These two methods are equivalent in selecting the data
    athletesCountry = athleteData[athleteData['NOC'] == countryCode]
    #athletesCountry = athleteData.groupby('NOC').get_group(countryCode)

    #Create two variables to hold the medal names
    #and the number of these medals for the country
    medals = ["Gold", "Silver", "Bronze"]
    medalsCountry = [0,0,0]

    #Get the length of the data frame when grouped by both country and medal
    #to get the number of medals.
    #Note that this could be done on one line, but split for clarity
    medalsCountry[0] = len(athletesCountry.groupby('Medal').get_group('Gold'))
    medalsCountry[1] = len(athletesCountry.groupby('Medal').get_group('Silver'))
    medalsCountry[2] = len(athletesCountry.groupby('Medal').get_group('Bronze'))

    #Plot the figure as a bar chart with labels
    plt.figure()
    fig4 = plt.bar(medals, medalsCountry)
    plt.title(f"Medal Wins for {countryCode}")
    plt.xlabel("Medals")
    plt.ylabel("Number of Medals")

    return fig4