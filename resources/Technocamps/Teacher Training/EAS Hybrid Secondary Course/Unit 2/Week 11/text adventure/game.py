import map

class Game:
    def __init__(self):
        self.mapObj = map.Map()
        self.mapObj.importRooms()
        self.currentRoom = None

    def gameLoop(self):
        self.gameRunning = True

        self.blurbCheck = True

        while self.gameRunning == True:

            if self.blurbCheck == True:
                self.currentRoom.printBlurb()
                self.blurbCheck = False

            decision = input("What now? ")

            self.moveRooms(decision)
            

    def moveRooms(self, direction):
        newRoom = self.currentRoom.findRoom(self.mapObj, direction)

        if newRoom == None:
            message = "You can't go {}!"
            print(message.format(direction))

        else:
            message = "You go {}!"
            print(message.format(direction))
            self.currentRoom = newRoom
            self.blurbCheck = True
            

    def gameStart(self):
        print("Would you like to start a new game? Y/N")
        if input().upper() == "Y":
            self.currentRoom = self.mapObj.getRoomAt(1, 0)
            gameObj.gameLoop()

gameObj = Game()
gameObj.gameStart()
        
