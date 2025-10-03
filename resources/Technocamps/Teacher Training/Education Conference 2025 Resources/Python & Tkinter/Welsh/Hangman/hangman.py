#Hangman

import os

#Mewnforio dependencies
from random import randint


def main():

    #Neges croeso
    print("Croeso i Hangman!")
    dechrau_gem()

def dechrau_gem():

    global bywydau

    bywydau = 9

    dyfaliadau = []

    gair = gair_ar_hap()

    cynnydd = "_ " * len(gair)

    argraffu(dyfaliadau, cynnydd)

    guessing(progress, word, guessed)

    play_again()



def gair_ar_hap():

    ffeil_geiriau = open(os.path.dirname(os.path.abspath(__file__)) + "/wordlist.txt","r")
    data_geiriau = ffeil_geiriau.read()
    rhestr_geiriau = data_geiriau.split("\n")

    rhif = randint(0, len(rhestr_geiriau))
    gair = rhestr_geiriau[rhif]

    return gair



def gwirio(gair, dyfaliad, cynnydd):

    global bywydau

    darganfod_llythyren = False

    for llythyren in gair:

        if llythyren == dyfaliad:

            darganfod_llythyren = True

            indecs = word.index(letter)

            i = indecs * 2

            cynnydd = cynnydd[:i] + cynnydd[indecs] + cynnydd[i+1:]

            gair = gair[:indecs] + " " + gair[indecs+1:]

    if darganfod_llythyren == False:
        bywydau -= 1

    return cynnydd



def dyfalu(gair, cynnydd, dyfaliadau):
    
    global bywydau

    while (("_" in cynnydd) and (bywydau > 0)):

        yn_dyfalu = True
        while yn_dyfalu:

            dyfaliad = input("\nDyfalu Llythyren: ")

            if len(dyfaliad) != 1:
                print("Dyfalu 1 llythyren!")

            elif dyfaliad.isalpha() == False:
                print("Rhaid dyfalu llythrennau!")

            elif dyfaliad in dyfaliadau:
                print("Barod wedi dyfalu hyn!")

            else:
                yn_dyfalu = False

        cynnydd = gwirio(gair, cynnydd, dyfaliad)
        dyfaliadau.append(dyfaliad)
        argraffu(dyfaliadau, cynnydd)

        

def argraffu(dyfaliadau, cynnydd):
    
    print("\n" + cynnydd)

    str_dyfaliadau = ""

    for i in dyfaliadau:

        str_dyfaliadau = str_dyfaliadau + i + " "

    print("\nWedi Dyfalu:\n" + str_dyfaliadau)



def chwarae_eto():

    gwiriad_ailchwarae = True

    while gwiriad_ailchwarae == True:

        ailchwarae = input("\nWyt ti eisiau chwarae eto? Y/N\n")

        if ailchwarae.upper() == "Y":
            dechrau_gem()

        elif ailchwarae.upper() == "N":
            gwiriad_ailchwarae = False
            print("Diolch am chwarae!")

        else:
            print("Plis rhoi mewnbwn dilys!")

main()
