

def moveRoom(direction, currentLocation, gameRooms, blurbCheck):
    newX, newY = None, None

    for i, item in enumerate(gameRooms):
        if gameRooms[i]["Room"] == currentLocation:
            if direction == "North":
                newX = gameRooms[i]["xCoordinate"]
                newY = gameRooms[i]["yCoordinate"] - 1
            elif direction == "East":
                newX = gameRooms[i]["xCoordinate"] + 1
                newY = gameRooms[i]["yCoordinate"]
            elif direction == "South":
                newX = gameRooms[i]["xCoordinate"]
                newY = gameRooms[i]["yCoordinate"] + 1
            elif direction == "West":
                newX = gameRooms[i]["xCoordinate"] - 1
                newY = gameRooms[i]["yCoordinate"]
            break

    oldRoom = currentLocation

    for i, item in enumerate(gameRooms):
        if (gameRooms[i]["xCoordinate"] == newX) and (gameRooms[i]["yCoordinate"] == newY):
            currentLocation = gameRooms[i]["Room"]
            blurbCheck = True
            # Break required to leave for loop once correct room found
            break

    if oldRoom == currentLocation:
        print("You are unable to travel {}!\n".format(direction))


    return currentLocation, blurbCheck