import matplotlib.pyplot as plt

# Task 2 is to teach basic plotting with matplotlib
def task(pokemonData):

    # Create a new figure (this alow multiple window to be plotted at once)
    # and plot two of the DataFrame columns: Year and Value
    plt.figure()
    fig1 = plt.scatter(pokemonData.get('attack'), pokemonData.get('defense'))
    plt.figure()
    fig2 = plt.scatter(pokemonData.get('sp_attack'), pokemonData.get('sp_defense'))
    plt.figure()
    fig2 = plt.scatter(pokemonData.get('attack'), pokemonData.get('hp'))
    plt.figure()
    fig2 = plt.scatter(pokemonData.get('defense'), pokemonData.get('hp'))
    # Return the required values to the main program
    return fig1, fig2