import matplotlib.pyplot as plt

# Task 4 is plotting the data from Task3b.py nicely, with a title and axis labels, and control over the points.
def task(dates, concentration):
    plt.figure()
    #fig.add_subplot()
    fig4 = plt.scatter(dates, concentration.get('Value'), s=0.5, marker='.')

    plt.title("Atmospheric CO2 Concentrations")
    plt.xlabel("Year")
    plt.ylabel("CO2 (Parts Per Million)")

    return fig4