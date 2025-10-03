# Import the Python classes Map, random and Entity
import Map
import random
import Entity

# Create class called Game to include all core functions of the Game
class Game:

    # Initialise the Game class with the current room as a parameter and also load
    # the gameplay essential objects before starting: the map, the rooms, the player
    def __init__(self):
        self.currentRoom = None
        self.mapObj = Map.Map()
        self.mapObj.importRooms()
        self.playerObj = Entity.Player()

    def gameStart(self):

        # Ask the user if they would like to start a new game (this is a placeholder for loading a saved game)
        print("Would you like to start a new game? Y/N")
        if input().upper() == "Y":
            # Create an object of the Game class - this is a necessary step in object-oriented programming,
            # like calling main() after defining functions.
            # Pass into the new game the initial room - this cannot be a default parameter of the constructor
            # as the map object has not been created yet.
            self.currentRoom = self.mapObj.getRoomAt(1, 0)

            # Call the main game loop method of the object created to begin.
            gameObj.gameLoop()

    # Define game loop method to run the primary game function
    def gameLoop(self):

        # Initialise a Boolean value to keep loop running - this could be used to create a Game Over scenario
        self.gameRunning = True

        # Initialise a Boolean value to check whether blurb should be shown
        # - this will avoid the room blurb reappearing for every action taken within a room
        self.blurbCheck = True

        # Run main game loop so long as Boolean value gameRunning is still True
        while self.gameRunning == True:

            # Check if blurb should be shown (i.e. has the user just moved into a new room)
            # Then return the Boolean to false in case next user decision is invalid
            if self.blurbCheck == True:
                self.currentRoom.printBlurb()
                self.blurbCheck = False

            # Print to the screen how many enemies are in the room
            self.currentRoom.printEnemies()

            # Ask user to enter a decision of what to do next
            decision = input("What now?")

            # If user enters NORTH as a decision, call the getNewRoom method tp move to a room
            # due west of current room - if this is possible
            if "NORTH" in decision.upper():
                self.getANewRoom("North")

            # If user enters EAST as a decision, call the getNewRoom method tp move to a room
            # due west of current room - if this is possible
            elif "EAST" in decision.upper():
                self.getANewRoom("East")

            # If user enters SOUTH as a decision, call the getNewRoom method tp move to a room
            # due west of current room - if this is possible
            elif "SOUTH" in decision.upper():
                self.getANewRoom("South")

            # If user enters WEST as a decision, call the getNewRoom method tp move to a room
            # due west of current room - if this is possible
            elif "WEST" in decision.upper():
                self.getANewRoom("West")

            # Attack a nearby enemy at random IF there are enemies present in the room
            # This is achieved by passing the list of room enemies from the currentRoom object
            # into the attackEnemy method of the Player object
            elif "ATTACK" in decision.upper():
                if len(self.currentRoom.roomEnemies) > 0:
                    self.playerObj.attackEnemy(self.currentRoom.roomEnemies[random.randint(0, len(self.currentRoom.roomEnemies) - 1)])

            # If user enters anything else then print that it can't be done
            else:
                print("I can't do that...")


    # Attempt to get a new room in th direction specified by the user.
    # IF there is no room in that direction a None value will be returned and a message printed to the screen.
    # IF there is a room then set that to be the current room and print a message that the player moves rooms.
    def getANewRoom(self, direction):

        newRoom = self.currentRoom.findNewRoom(self.mapObj, direction)

        # If a None value is received instead of a Room object then print that it is not possible to travel North
        if newRoom == None:
            message = "You can't go {}!"
            print(message.format(direction))

        # If a Room object is returned then print that the player travels in that direction,
        # then replace the currentRoom object with the newRoom object and set blurbCheck to True
        # as the player will be entering a new room
        else:
            message = "You go {}!"
            print(message.format(direction))
            self.currentRoom = newRoom
            self.blurbCheck = True


gameObj = Game()
gameObj.gameStart()