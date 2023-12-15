import zombiedice
import random


class MyZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll()
            else:
                break


class randomStopZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if random.randint(1,2) == 1:
                zombiedice.roll()
            else:
                break


class StopsAfterTwoShotgunsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()
        brains = 0
        shotguns = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']
            if shotguns < 2:
                diceRollResults = zombiedice.roll()
            else:
                break


class OneToFourZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        brains = 0
        shotguns = 0
        for i in range(random.randint(1, 4)):
            diceRollResults = zombiedice.roll()
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']
            if shotguns >= 2:
                break


class MoreShotgunThanBrainZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        shotguns = 0
        while shotguns < brains:
            diceRollResults = zombiedice.roll()
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']


zombies = (
    MyZombie(name='My Zombie Bot'),
    randomStopZombie(name='Ron Burgundy'),
    StopsAfterTwoShotgunsZombie(name='Veronica Corningstone'),
    OneToFourZombie(name='Brick Tamland'),
    MoreShotgunThanBrainZombie(name='Brian Fantana')
)

zombiedice.runWebGui(zombies=zombies, numGames=1000)
