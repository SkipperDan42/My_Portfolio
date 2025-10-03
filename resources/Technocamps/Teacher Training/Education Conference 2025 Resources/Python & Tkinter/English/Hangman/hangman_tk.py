#Hangman
import os

#Import dependencies
from random import randint
import tkinter as tk
from tkinter import messagebox


def main():

    global root, canvas
      
    # Create the main window
    root = tk.Tk()
    root.title("Hangman")

    #Initialise game
    game_start()
    root.mainloop()

def game_start():

    # Define no_of_lives, empty list of guessed letters, and word to guess
    global lives, guessed, word
    lives = 6
    guessed = []
    word = random_word()

    gui_start()


def random_word():

    wordFile = open(os.path.dirname(os.path.abspath(__file__)) + "/wordlist.txt","r")
    wordData = wordFile.read()
    wordList = wordData.split("\n")

    number = randint(0,len(wordList))
    word = wordList[number]

    return word


def gui_start():

    global root, lives, guessed, word
    global canvas, word_label, lives_label, guessed_label, guess_entry

    # Create the canvas for drawing the hangman
    canvas = tk.Canvas(root, width=300, height=300, bg='white', highlightthickness=0)
    canvas.create_image(0, 0, image=bg_image, anchor='nw')
    canvas.grid(column=0, row=0)

    # Create Retry and Exit Buttons
    retry_button = tk.Button(root, text="Retry", command=lambda:retry_game())
    retry_button.grid(column=0, row=5)
    exit_button = tk.Button(root, text="Exit", command=lambda:exit_game())
    exit_button.grid(column=0, row=6)

    # Allows user to press enter key to input guess
    root.bind("<Return>", lambda event: check_guess())

    # Draw the scaffold
    canvas.create_line(20, 280, 120, 280)
    canvas.create_line(70, 280, 70, 20)
    canvas.create_line(70, 20, 170, 20)
    canvas.create_line(170, 20, 170, 50)

    # Create a label for displaying the word
    word_label = tk.Label(root, text=" ".join(["_" for letter in word]))
    word_label.grid(column=0, row=1)

    # Create a label for displaying the number of lives remaining
    lives_label = tk.Label(root, text="Lives remaining: {}".format(lives))
    lives_label.grid(column=0, row=2)

    # Create a label for displaying the letters guessed so far
    guessed_label = tk.Label(root, text="Guessed letters: ")
    guessed_label.grid(column=0, row=3)

    # Create an entry for the user to guess a letter
    guess_entry = tk.Entry(root)
    guess_entry.grid(column=0, row=4)


def check_guess():

    global root, lives, guessed, word, word_label, lives_label, guessed_label, guess_entry
    
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)
    
    # Check if the guess is a single letter or if the guess has already been guessed
    if len(guess) != 1 or not guess.isalpha() or guess in guessed:
        return
    
    guessed.append(guess)
    guessed_label.config(text="Guessed letters: {}".format(" ".join(guessed)))
    
    # Check if the guess is in the word
    if guess in word:
        word_list = list(word_label["text"])
        for i in range(len(word)):
            if word[i] == guess:
                word_list[2*i] = guess
        word_label.config(text="".join(word_list))
        
        # Check if the user has won
        if "_" not in word_list:
            messagebox.showinfo("Hangman", "You win!")
            guess_entry.config(state=tk.DISABLED)
            return
    
    # If the guess is not in the word, decrement the number of lives remaining
    else:
        lives -= 1
        lives_label.config(text="lives remaining: {}".format(lives))
        
        # Draw the hangman
        if lives == 5:
            canvas.create_oval(140, 50, 200, 110)
        elif lives == 4:
            canvas.create_line(170, 110, 170, 170)
        elif lives == 3:
            canvas.create_line(170, 130, 140, 140)
        elif lives == 2:
            canvas.create_line(170, 130, 200, 140)
        elif lives == 1:
            canvas.create_line(170, 170, 140, 190)
        elif lives == 0:
            canvas.create_line(170, 170, 200, 190)
            messagebox.showinfo("Hangman", "You lose! The word was '{}'".format(word))
            guess_entry.config(state=tk.DISABLED)


def retry_game():

    global canvas, guessed_label, word_label, lives_label

    # Destroy canvas and clear labels    
    canvas.destroy()
    guessed_label.config(text="")
    word_label.config(text="")
    lives_label.config(text="")

    #Restart Game
    game_start()

  
def exit_game():

    #Destroy root (i.e. entire GUI)
    global root
    root.destroy()


main()
