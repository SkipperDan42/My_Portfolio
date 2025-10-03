#Import other python files for this program
import save_handling as sh
import load_assets as la
import actions as act

#Main loop upon program start
def main(playerItems):
    #Check whether the player would like to play a new game or load a save
    newOrLoad = input("Would you like to start a 'New' game or 'Load' a previous save?\n")

    #If player answers new game then run the new_game function from save_handling
    #to create a save file and return the player name - then launch gameplay function
    if newOrLoad.upper() == "NEW":
        playerName = sh.new_game()
        gameplay(playerName, "Reception", playerItems)

    #If player answers load game then open game saves list and check for matching
    #save game.
    elif newOrLoad.upper() == "LOAD":
        gameSavesList = open("game_saves_list.txt", "r")
        tempNames = str(gameSavesList.read().split("\n"))

        #If list is empty then report no saves, if saves exist then run the load_game
        #function from save_handling to attempt loading in a save. Return the player name,
        #current location and inventory - then launch gameplay function to return to save.
        if len(tempNames) > 0:
            playerName,currentLocation,playerItems = sh.try_login(tempNames)
            gameplay(playerName,currentLocation,playerItems)
        else:
            print("No save games exist!")
            main()

    #Else if player answers neither NEW nor LOAD then reply invalid and repeat.
    else:
        print("\nInvalid entry. Try again.\n")
        main()

#Gameplay function handles all gameplay elements
def gameplay(playerName,currentLocation,playerItems):

    #Define boolean checks required for gameplay
    roomCheck = True
    blurbCheck = True

    #While loop continues gameplay indefinitely until exited
    while roomCheck == True:

        #Upon each new loop check whether the room blurb should be displayed.
        #This is only necessary when entering a new location.
        if blurbCheck == True:
            for i,item in enumerate(gameRooms):
                if gameRooms[i]["Room"] == currentLocation:
                    print(gameRooms[i]["Blurb"])

        #Define blurbCheck as False until a command is entered that requires
        #a new blurb to be broadcast.
        blurbCheck = False

        #The primary input question during each loop of the game, allowing the
        #player to decide their next move.
        decision = input("What now?\n")

        #Check if player decision includes NORTH, if so have character head to
        #new location north of current location when possible, otherwise skip to
        #next decision.
        if "NORTH" in decision.upper():
            currentLocation, blurbCheck = act.moveRoom("North", currentLocation, gameRooms, blurbCheck)

        #Check if player decision includes EAST, if so have character head to
        #new location east of current location when possible, otherwise skip to
        #next decision.
        elif "EAST" in decision.upper():
            currentLocation, blurbCheck = act.moveRoom("East", currentLocation, gameRooms, blurbCheck)


        #Check if player decision includes SOUTH, if so have character head to
        #new location south of current location when possible, otherwise skip to
        #next decision.
        elif "SOUTH" in decision.upper():
            currentLocation, blurbCheck = act.moveRoom("South", currentLocation, gameRooms, blurbCheck)

        #Check if player decision includes WEST, if so have character head to
        #new location west of current location when possible, otherwise skip to
        #next decision.
        elif "WEST" in decision.upper():
            currentLocation, blurbCheck = act.moveRoom("West", currentLocation, gameRooms, blurbCheck)

        #HELP command opens list of common actions that can be used within rooms
        elif "HELP" in decision.upper():
            with open("help.txt") as help:
                for line in help:
                    print(line)

        #BAG command displays the current character inventory to the player
        elif "BAG" in decision.upper():
            for item in playerItems:
                print(playerItems[item])

        #Save command calls the save_game function within save_handling to write
        #the current progress to file
        elif "SAVE" in decision.upper():
            sh.save_game(playerName,currentLocation,playerItems)

        #If none of the common commands have been inputted then loop through the
        #gameActions file to find if player command matches any unique room actions.
        #If match is found print the blurb and if there is an item add to inventory.
        else:
            for i,item in enumerate(gameActions,start=1):
                if gameActions[i]["Room"] == currentLocation and gameActions[i]["Command"].upper() in decision.upper():
                    print(gameActions[i]["Blurb"])
                    if gameActions[i]["Item"] != "":
                        for j,item in enumerate(gameItems,start=1):
                            if gameItems[j]['Item Name'] == gameActions[i]["Item"]:
                                playerItems[len(playerItems) + 1] = gameItems[item]
                                break
                    break

#Initialise variables on game start
playerItems = {}
gameRooms = {}
gameActions = {}
gameItems = {}

#Load game assets using functions within load_assets
gameRooms = la.load_rooms(gameRooms)
gameActions = la.load_actions(gameActions)
gameItems = la.load_items(gameItems)

#Begin the main game loop
main(playerItems)

