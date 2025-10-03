#Load rooms function loops through all lines in the rooms file, saving each as a new
#room in the gameRooms dictionary. Values in rooms file are seperated by ":", saving
#each to a new value in the individual room dictionary.
def load_rooms(gameRooms):
    with open("Rooms.csv") as file:
        i = 0
        for j,line in enumerate(file):
            if (line != "\n") and (j != 0):
                (Room, xCoordinate, yCoordinate, Blurb) = line.replace("\n", "").split(",")
                gameRooms[i] = {"Room": Room, "xCoordinate": int(xCoordinate), "yCoordinate": int(yCoordinate), "Blurb": Blurb}
                i += 1
        return gameRooms


#Load actions function loops through all lines in the actions file, saving each as a new
#action in the gameActions dictionary. Values in actions file are seperated by ":", saving
#each to a new value in the individual actions dictionary.
def load_actions(gameActions):
    i = 1
    with open("actions.txt") as f:
        for line in f:
            (Room, Command, Action, Item, Blurb) = line.replace("\n", "").split(":")
            gameActions[i] = {"Room": Room, "Command": Command, "Action": Action, "Item": Item, "Blurb": Blurb}
            i += 1
    return gameActions


#Load items function loops through all lines in the items file, saving each as a new
#item in the gameItems dictionary. Values in items file are seperated by ":", saving
#each to a new value in the individual item dictionary.
def load_items(gameItems):
    i = 1
    with open("items.txt") as f:
        for line in f:
            (itemName, value) = line.replace("\n", "").split(":")
            gameItems[i] = {"Item Name": itemName, "Value": value}
            i += 1
    return gameItems