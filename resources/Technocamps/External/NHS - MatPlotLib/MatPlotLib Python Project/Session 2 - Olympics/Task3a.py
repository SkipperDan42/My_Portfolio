import matplotlib.pyplot as plt

# Task 2 is to teach basic plotting with matplotlib
def task(athleteData):

    # Create a new figure (this alow multiple window to be plotted at once)
    # and plot two of the DataFrame columns.
    plt.figure()
    fig1 = plt.scatter(athleteData.get('Year'), athleteData.get('Age'))
    plt.figure()
    fig2 = plt.scatter(athleteData.get('Year'), athleteData.get('Height'))
    plt.figure()
    fig3 = plt.scatter(athleteData.get('Year'), athleteData.get('Weight'))
    plt.figure()
    fig4 = plt.scatter(athleteData.get('Age'), athleteData.get('Height'))
    plt.figure()
    fig5 = plt.scatter(athleteData.get('Age'), athleteData.get('Weight'))
    # Return the required values to the main program
    return fig1, fig2, fig3, fig4, fig5