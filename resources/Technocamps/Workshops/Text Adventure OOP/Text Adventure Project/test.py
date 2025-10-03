import Entity
import Map

gameMap = Map.Map()

gameMap.importRooms()

currentRoom = gameMap.getRoomAt(1, 1)
currentRoom = currentRoom.goNorth(gameMap)
print(currentRoom.name)

player = Entity.Player()
enemy = Entity.Enemy("Vampire")

player.attackEnemy(enemy)
