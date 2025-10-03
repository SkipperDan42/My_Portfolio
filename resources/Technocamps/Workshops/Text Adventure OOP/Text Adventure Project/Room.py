# Import Entity class so that each room can be populated with enemies
# Import the random class so that random numbers of enemies can be generated
import Entity
import random

# Define Room class to define the attributes and methods of each room
class Room:

    # Each object is initialised with any necessary attributes
    # As these are retrieved from a source file a correction is applied to ensure the right types.
    def __init__(self, name, xCoordinate, yCoordinate, blurb):
        self.name = self.sourceFileCorrection(name)
        self.xCoordinate = self.sourceFileCorrection(xCoordinate)
        self.yCoordinate = self.sourceFileCorrection(yCoordinate)
        self.blurb = self.sourceFileCorrection(blurb)
        self.loadEnemies()


    # Correct the values received from the source file,
    # to change empty fields denoted by underscores to "None" values
    # to cast any numerical fields to become integer type
    def sourceFileCorrection(self, input):
        if input == "_":
            return None
        elif input.isdigit():
            return int(input)
        else:
            return input


    # Print the blurb that describes each room
    def printBlurb(self):
        print(self.blurb)


    # The goToNewRoom method allows the player to move between rooms
    # - the coordinates of the current room are used to calculate the coordinates of the adjacent room
    #   in the desired direction
    # - the new coordinates are passed to the mapObj method getRoom, in order to retrieve the new Room object
    # - this object is then returned from this method
    def findNewRoom(self, mapObj, direction):
        newXCoordinate = self.xCoordinate
        newYCoordinate = self.yCoordinate

        if direction == "North":
            newYCoordinate = newYCoordinate - 1
        elif direction == "East":
            newXCoordinate = newXCoordinate + 1
        elif direction == "South":
            newYCoordinate = newYCoordinate + 1
        elif direction == "West":
            newXCoordinate = newXCoordinate - 1

        return mapObj.getRoomAt(newXCoordinate, newYCoordinate)

    # Load the enemies within each room. This method is run  at the beginning of the game when the rooms are created.
    def loadEnemies(self):
        # Create a new object variable of type list to hold the enemies for each room
        self.roomEnemies = []

        # Randomly generate the number of enemies within the room
        numberOfEnemies = random.randint(0, 3)

        # For each enemy use the createRandomEnemy method and append it to the list of enemies in the room
        # Pass the value i into the enemy entity to give each enemy in the room a unique ID
        for i in range(numberOfEnemies):
            newEnemy = Entity.Enemy(i)
            newEnemy.createRandomEnemy()
            self.roomEnemies.append(newEnemy)


    # Print the number of enemies in a room and the type of each enemy
    def printEnemies(self):

        # Create an empty list to store the alive enemies within the method
        # This implementation ensures the dead enemies are still present - this will be important if we implement loot.
        aliveEnemies = []

        # For each enemy within the list of enemies in the room, if they are alive then
        # - Add each to the list of alive enemies
        # - Add the index of each alive enemy from the list of all enemies to a new list
        #   (this allows us to track which enemies from the list of all enemies are alive)
        for enemy in self.roomEnemies:
            if enemy.health > 0:
                aliveEnemies.append(enemy)

        # Create a string that says however many alive enemies are still in the room
        printOut = "There are {} enemies in the room.".format(len(aliveEnemies))

        # For each enemy that is alive, create a string that shows their initial index and type
        # then add this to the string above
        for i,enemy in enumerate(aliveEnemies):
            enemyString = " Enemy {} is a {}.".format(enemy.enemyID, enemy.type)
            printOut += enemyString

        # Print the string
        print(printOut)