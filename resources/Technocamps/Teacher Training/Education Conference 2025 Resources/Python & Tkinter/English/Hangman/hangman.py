#Hangman

import os

#Import dependencies
from random import randint


def main():

    #Welcome message
    print("Welcome to Hangman\n")

    #Initialise game
    game_start()

def game_start():

    global lives

    lives = 9

    #Define guess list as empty ready for use (also clears in repeat games)
    guessed = []

    #Pick random word from file
    word, progress = random_word()

    #Print out empty progress before game
    print_out(guessed,progress)

    #Commence guessing loop
    guessing(progress, word, guessed)

    #Once loop is complete ask to play again
    play_again()



def random_word():

    wordFile = open(os.path.dirname(os.path.abspath(__file__)) + "/wordlist.txt","r")

    wordData = wordFile.read()

    wordList = wordData.split("\n")

    number = randint(0,len(wordList))

    word = wordList[number]

    progress = "_ "*len(word)

    return word, progress



def check_word(word,guess,progress):

    global lives

    letter_found = False

    for element in word:

        if element == guess:

            letter_found = True

            index = word.index(element)

            i = index * 2

            progress = progress[:i] + word[index] + progress[i+1:]

            word = word[:index] + " " + word[index+1:]

    if letter_found == False:
        lives -= 1

    return progress



def guessing(progress, word, guessed):

    global lives

    while (("_" in progress) and (lives > 0)):

        guessCheck = True

        while guessCheck == True:

            
            guess = input("\nEnter a letter: ")
            

            if len(guess) != 1:
                print("Enter only 1 letter!")
            elif guess.isalpha() == False:
                print("Enter a letter!")
            elif guess in guessed:
                print("You already tried that letter!")
            else:
                guessCheck = False
    
        progress = check_word(word,guess,progress)

        guessed.append(guess)

        print_out(guessed,progress)

        

def print_out(guessed,progress):

        guessStr = ""
        
        print("\n" + progress)

        for i in guessed:
            guessStr = guessStr + i

        print("\nGuessed Letters\n" + guessStr)



def play_again():

    replayCheck = True

    while replayCheck == True:

        replay = input("\nWould you like to play again? Y/N\n")

        if replay.upper() == "Y":
            game_start()

        elif replay.upper() == "N":
            replayCheck = False
            print("Thank you for playing!")

        else:
            print("Please enter a valid input!")

main()
