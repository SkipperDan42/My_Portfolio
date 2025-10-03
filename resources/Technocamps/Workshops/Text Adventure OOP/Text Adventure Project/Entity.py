# Import random class file so that methods can use random values
import random

# Define Entity class to define the attributes and methods of each entity
class Entity:

    # Each entity is initialised with any necessary attributes of an entity
    def __init__(self, health = 100, strength = 1, damage = 1, luck = 1, weapon = None):
        self.health = health        # The current health of an entity
        self.strength = strength    # The strength of an enemy (increases as entity levels up)
        self.damage = damage        # The damage an enemy causes (denoted by their weapon)
        self.luck = luck            # How lucky an entity is (this will decide the success of their attack)
        self.weapon = weapon        # The weapon an enemy has equipped


# Define the Player subclass to define the attributes and methods unique to the player
class Player(Entity):

    # The player entity is initialised with any necessary attributes unique to the player (experiencePoints)
    # Additionally all attributes that belong to all entities are initialised using the super() method
    def __init__(self, health = 100, strength = 1, damage = 1, luck = 1, weapon = None, experiencePoints = 0):
        super().__init__(health, strength, damage, luck, weapon)
        self.experiencePoints = experiencePoints

    # This method calculates the success of and damage caused by an attack on an enemy
    # This damage is passed to the enemies damageFromPlayer method to calculate the effect on the enemy.
    # The enemy then returns the number of experience points gained from the attack.
    def attackEnemy(self, enemy):
        diceRoll = random.randint(0,19)
        attackSuccess = self.luck * diceRoll
        attackDamage = (self.strength * self.damage * attackSuccess) / enemy.strength
        self.experiencePoints += enemy.damageFromPlayer(round(attackDamage), self.experiencePoints)


# Define the Enemy subclass to define the attributes and methods unique to the enemies
class Enemy(Entity):

    # The enemy entity is initialised with any necessary attributes unique to the enemy (enemyID, type, experienceGiven)
    # Additionally all attributes that belong to all entities are initialised using the super() method
    def __init__(self, enemyID, health = 100, strength = 1, damage = 1, luck = 1, weapon = None, type = None):
        super().__init__(health, strength, damage, luck, weapon)
        self.enemyID = enemyID
        self.type = type
        self.experienceGiven = strength * damage

    # Randomly chose between enemy types to create the enemy with randomised stats of that type
    def createRandomEnemy(self):

        # Randomly choose between the enemy types
        self.type = random.choice(["Janitor", "Teacher"])

        # Depending on the type selected, set the enemy attributes accordingly (using random ranges)
        # This should ideally be called from a file of enemy types.
        if type == "Janitor":
            self.weapon = random.choice([None, "Mop", "Hammer"])
            self.health = random.randint(25, 50)
            self.strength = random.uniform(0.8, 1.2)
            self.luck = random.uniform(0.5, 1.0)

        elif type == "Teacher":
            self.weapon = random.choice([None, "Pens", "Meter Rule"])
            self.health = random.randint(40, 60)
            self.strength = random.uniform(1, 2)
            self.luck = random.uniform(1.5, 2.0)

    # Remove the damage caused by the player attack from the health of the enemy.
    # If this reduces the enemy to 0 health then return experienceGiven to the player,
    # otherwise return 0.
    def damageFromPlayer(self, attackDamage,experiencePoints):
        self.health -= attackDamage

        if self.health <= 0:
            print("Enemy Defeated!")
            return self.experienceGiven
        else:
            print("Enemy {} HP: {}".format(self.enemyID, self.health))
            return 0