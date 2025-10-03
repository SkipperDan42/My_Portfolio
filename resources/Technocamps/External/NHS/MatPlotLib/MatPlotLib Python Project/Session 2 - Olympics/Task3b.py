import matplotlib.pyplot as plt

# Task 2 is to teach basic plotting with matplotlib
def task(athleteData):

    # Create a new figure (this allows multiple windows to be plotted at once)
    # and plot two of the DataFrame columns. This time adding labels.
    plt.figure()
    fig1 = plt.hist(athleteData[athleteData["Medal"] == "Gold"].get("Age"), 100, color="gold")
    plt.xlabel("Age of Athletes")
    plt.ylabel("Number of Gold Medal Winners")

    plt.figure()
    fig2 = plt.hist(athleteData[athleteData["Medal"].isna()].get("Age"), 100, color="black")
    plt.xlabel("Age of Athletes")
    plt.ylabel("Number of Gold Medal Winners")

    plt.figure()
    fig3 = plt.hist(athleteData[athleteData["Sport"] == "Gymnastics"].get("Height"),
                    100, color="red")
    plt.xlim(120, 240)
    plt.xlabel("Olympian Height")
    plt.ylabel("Number of Gymnasts")

    plt.figure()
    fig4 = plt.hist(athleteData[athleteData["Sport"] == "Basketball"].get("Height"),
                    100, color="black")
    plt.xlim(120, 240)
    plt.xlabel("Olympian Height")
    plt.ylabel("Number of Basketballers")

    # Return the required values to the main program
    return fig1, fig2, fig3, fig4