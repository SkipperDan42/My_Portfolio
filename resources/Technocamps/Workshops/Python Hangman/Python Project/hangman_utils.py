"""
hangman_utils.py

This module provides utility functions for the Hangman Game; these include
getting a random word from file and printing out the state of the game.
"""

# Initialise dependencies
from random import randint as rand
import os 



def get_random_word():
    """
    Gets a random word from a file.

    Will return both the random word as well as underscores (seperated by
    progress)for the number of letters present in that word.

    Parameters:

    Returns:
        String: The random word.
        String: A number of underscores (seperated by progress) equal to the
                word length.

    Raises:
        FileNotFoundError: The word file could not be found..
    """

    word = ""
    progress = ""

    try:
        file_name = "wordlist.txt"
        file_directory = os.path.dirname(os.path.abspath(__file__))

        wordFile = open(file_directory + "/" + file_name, "r")
        wordData = wordFile.read()
        wordList = wordData.split("\n")

        number = rand(0,len(wordList))
        word = wordList[number]

        progress = "_ "*len(word)

    except FileNotFoundError:
        print(f"Cannot find file {file_name}")

    finally:
        return word, progress



def print_game_state(current_word_state, letters_guessed):
    """
    Prints the state of the game.

    Will print out the current state of the word being guessed, as well as
    the letters that have already been guessed.

    Parameters:
        current_word_state (String):    The word with underscores and guessed
                                        letters filled in
        letters_guessed (List):         The list of letters that have been
                                        guessed so far

    Returns:
        String: The random word.
        String: A number of underscores equal to the word length.

    Raises:
        ErrorType: Description of the error raised.
    """

    guessed_str = ""
    
    print("\nYour Attempt:\n" + current_word_state)

    for i in letters_guessed:
        guessed_str = guessed_str + i

    print("\nGuessed Letters:\n" + guessed_str)

    