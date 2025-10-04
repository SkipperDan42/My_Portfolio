import pandas as pd


# Task 1 is to teach opening a csv with pandas, defining columns, and printing to the screen
def task():

    #Read in the desired csv file:
    # - this will be stored as a pandas DataFrame
    # - this requires the name of the
    yearlyConcentration = pd.read_csv('Atmospheric CO2 Concentrations.csv', usecols=['Year', 'Month', 'Value'])
    print(yearlyConcentration)
    return yearlyConcentration