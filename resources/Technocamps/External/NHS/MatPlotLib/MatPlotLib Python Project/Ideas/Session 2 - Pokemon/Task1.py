import pandas as pd


# Task 1 is to teach opening a csv with pandas, defining columns, and printing to the screen
def task():

    #Read in the desired csv file:
    # - this will be stored as a pandas DataFrame
    # - this requires the name of the
    pokemonData = pd.read_csv('pokemon.csv', usecols=['pokedex_number', 'attack', 'sp_attack', 'defense', 'sp_defense' ,'hp', 'is_legendary'])
    print(pokemonData)
    return pokemonData