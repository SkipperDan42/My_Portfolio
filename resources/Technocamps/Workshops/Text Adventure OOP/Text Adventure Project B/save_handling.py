#Begin new game by first asking for a character name, then creating a file
#with the name of said character. Add the save file to the list of save files
#and return the player name so that the game can begin
def new_game():
    nameCheck = True
    while nameCheck == True:
        playerName = input("Please enter a character name:")
        if playerName.lower() in protected:
            print("This is a protected name, please choose another.\n")
        else:
            nameCheck = False

    playerName = playerName.replace(" "or".","_")
    saveFile = open(playerName+".txt","w")
    saveFile.close()
    gameSavesList = open("game_saves_list.txt", "a")
    gameSavesList.write(playerName+"\n")
    gameSavesList.close()
    return playerName


#Ask player for the character name and search the game saves list for said
#character.
def try_login(tempNames):
    playerName = input("\nWhat is your character name?\n")

    #If name is within saves list then call load_game functions
    if playerName in tempNames:
        currentLocation,playerItems = load_game(playerName)

    #Else report that save does not exist.
    else:
        print("This save does not exist!\n")

        #Loop to check if player would like to retry loading or return to main
        tryCheck = True
        while tryCheck == True:
            tryAgain = input("Would you like to try 'Again' or 'Return' to main menu?\n")
            if tryAgain.upper() == "AGAIN":
                tryCheck = False
                try_login(tempNames)
            elif tryAgain.upper() == "RETURN":
                #FIX THIS!
                tryCheck = False
    return playerName,currentLocation,playerItems


#Load game function opens the txt file with the name of the player character,
#first line of file is ignored as it is the character name, second line is saved
#as current location, the remaining lines are added to the player items dictionary.
def load_game(playerName):
    playerItems={}
    currentLocation = None
    with open(playerName+".txt") as saveFile:
        for i,line in enumerate(saveFile):
            if i == 1:
                pass
            elif i == 2:
                currentLocation = line.replace("\n","")
            else:
                (itemName, value) = line.replace("\n", "").split(":")
                playerItems[i-2] = {"Item Name": itemName, "Value": value}
            i += 1
    return currentLocation,playerItems


#Save game function takes the character name, current location and inventory, and
#writes it to a file with the name of the player character.
def save_game(playerName,currentLocation,playerItems):
    saveFile = open(playerName+".txt","w")
    saveData = playerName+"\n"+currentLocation
    for item in playerItems:
        saveData = saveData+"\n"+str(playerItems[item]["Item Name"])+":"+str(playerItems[item]["Value"])
    saveFile.write(saveData)
    saveFile.close()


protected = ["actions","items","rooms","help","map"]