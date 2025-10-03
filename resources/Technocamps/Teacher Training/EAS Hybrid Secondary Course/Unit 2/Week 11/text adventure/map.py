import room

class Map:

    def __init__(self):
        self.gameRooms = []

    def importRooms(self):
        with open("Rooms.csv") as roomFile:
            for i, line in enumerate(roomFile):
                if (line != "\n") and (i != 0):
                    (name, x, y, blurb) = line.replace("\n", "").split(",")
                    self.gameRooms.append(room.Room(name, x, y, blurb))

    def getRoomAt(self, x, y):
        for room in self.gameRooms:
            if (room.x == x) and (room.y == y):
                return room
            
        return None
                             
