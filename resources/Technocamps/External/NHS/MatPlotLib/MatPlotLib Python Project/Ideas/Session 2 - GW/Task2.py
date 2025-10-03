import matplotlib.pyplot as plt

# Task 2 is to teach basic plotting with matplotlib
def task(yearlyConcentration):

    # Create a new figure (this alow multiple window to be plotted at once)
    # and plot two of the DataFrame columns: Year and Value
    plt.figure()
    fig1 = plt.scatter(yearlyConcentration.get('Year'), yearlyConcentration.get('Value'))

    # Return the required values to the main program
    return fig1