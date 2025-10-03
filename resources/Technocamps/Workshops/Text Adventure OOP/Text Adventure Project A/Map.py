# Import the Room class so that the map can be populated with Room objects
import Room

# Create class called Map to handle the creation and retrieval of game rooms
class Map:

    # Initialise the Map class with a list of all game rooms as a parameter
    # - by creating and storing the rooms, they can be revisited without reverting to their initial conditions
    def __init__(self):
        self.gameRooms = []


    # Read the correctly formatted rooms file provided, defining each room by their name,
    # their x/y coordinates and the blurb that should print upon entering the room.
    # The file should have these parameters separated by the "," character,
    # and may have EMPTY lines between them. For each room create a Room object using
    # the parameters and store this within the gameRooms list
    def importRooms(self):
        with open("Rooms.csv") as roomFile:
            for i,line in enumerate(roomFile):
                if (line != "\n") and (i != 0):
                    (name, xCoordinate, yCoordinate, blurb) = line.replace("\n", "").split(",")
                    self.gameRooms.append(Room.Room(name, xCoordinate, yCoordinate, blurb))


    # Run through the gameRooms list or Room objects and check whether they match the coordinates provided.
    # - If a match is found, then return this Room object
    # - If there is no match then return the value None
    def getRoomAt(self, xCoordinate, yCoordinate):
        for entry in self.gameRooms:
            if (entry.xCoordinate == xCoordinate) and (entry.yCoordinate == yCoordinate):
                return entry
        return None