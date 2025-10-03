import pandas as pd


# Task 1 is to teach opening a csv with pandas,
# defining columns, and printing to the screen
def task():

    #Read in the desired csv file:
    # - this will be stored as a pandas DataFrame
    # - this requires the name of the
    athleteData = pd.read_csv('athlete_events.csv', usecols=['ID', 'Sex', 'Age', 'Height', 'Weight' ,
                                                                 'NOC', 'Year', 'Season' ,'Sport', 'Event',
                                                                 'Medal'])
    print(athleteData)
    return athleteData