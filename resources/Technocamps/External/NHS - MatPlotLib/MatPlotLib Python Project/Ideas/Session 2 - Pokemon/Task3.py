import pandas as pd
import matplotlib.pyplot as plt

# Task3b.py is to teach plotting more complicated data with matplotlib
# - opening a csv into two separate DataFrames with pandas,
# - adding a day column and converting into date format,
# - plotting both the DataFrame and date format with matplotlib
def task():
    yearMonth = pd.read_csv('Atmospheric CO2 Concentrations.csv', usecols=['Year', 'Month'])
    concentration = pd.read_csv('Atmospheric CO2 Concentrations.csv', usecols=['Value'])

    #dataSize = yearMonth.size

    #Create and fill a list of days -
    #The purpose of this is to assume each month begins on the first day, simplifying our data
    days = []
    for i in range(len(yearMonth.index)):
        days.append(1)

    #Insert the new days column into the yearsMonth DataFrame
    #Use pandas to convert this DataFrame into pandas Series of datetime objects
    yearMonth.insert(2, "Day", days)
    dates = pd.to_datetime(yearMonth, yearfirst=True)


    #Create a new figure and plot the datetime Series with the DataFrame (Value column)
    fig3 = plt.figure()
    fig3 = plt.scatter(dates, concentration.get('Value'))

    #Return the required values to the main program
    return dates, concentration, fig3