class Room:
    name = "N/A"
    x = 0
    y = 0
    blurb = "N/A"

    def __init__(self, name, x, y, blurb):
        self.name = self.sourceCorrection(name)
        self.x = self.sourceCorrection(x)
        self.y = self.sourceCorrection(y)
        self.blurb = self.sourceCorrection(blurb)

    def printBlurb(self):
        print(self.blurb)

    def findRoom(self, mapObj, direction):
        newX = self.x
        newY = self.y

        if direction == "north":
            newY -= 1

        elif direction == "east":
            newX += 1

        elif direction == "south":
            newY += 1
            
        elif direction == "west":
            newX -= 1

        return mapObj.getRoomAt(newX, newY)

    def sourceCorrection(self, inp):
        if inp == "_":
            return None
        elif inp.isdigit():
            return int(inp)
        else:
            return inp



        
