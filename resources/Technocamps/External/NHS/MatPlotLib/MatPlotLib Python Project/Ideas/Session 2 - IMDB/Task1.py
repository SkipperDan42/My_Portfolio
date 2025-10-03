import pandas as pd


# Task 1 is to teach opening a csv with pandas, defining columns, and printing to the screen
def task():

    #Read in the desired csv file:
    # - this will be stored as a pandas DataFrame
    # - this requires the name of the
    imdbData = pd.read_csv('imdb_top_1000.csv', usecols=['Released_Year', 'Runtime', 'Genre', 'IMDB_Rating', 'Gross'])
    print(imdbData)
    return imdbData