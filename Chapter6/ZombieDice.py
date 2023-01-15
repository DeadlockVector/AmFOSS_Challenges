import zombiedice

#for first bot
#deciding to continue or not
import random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        #REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        shotguns = 0
        brains = 0
        while brains>shotguns:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            
            diceRollResults = zombiedice.roll()

            
        

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)

'''
Bot1)
Randomly decides to roll or not
while diceRollResults is not None:
            #rolling
            diceRollResults = zombiedice.roll()
            val = random.randint(0, 1)
            if val == 1:
                continue

            elif val == 0:
                #breaking loop
                #when val is 0
                break

Bot2)
Stop rolling after getting 2 brains
brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains >= 2:
                break
                
            else:
                #rolling again
                #if we don't we dont' have 2 brains
                diceRollResults = zombiedice.roll() 

Bot3)
Stop rolling after getting 2 shotguns
shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']

            if shotguns >= 2:
                break
                
            else:
                #rolling again
                #if we don't we dont' have 2 brains
                diceRollResults = zombiedice.roll() 

Bot4)
Decide to roll 1 to 4 times
Stop if we get 2 shotguns
shotguns = 0
        for i in range(random.randint(1, 4)):
            if diceRollResults is not None:
                shotguns += diceRollResults['shotgun']
                
            if shotguns >= 2:
                break
            
            diceRollResults = zombiedice.roll()

Bot5)
Stop rolling after rolling more shotguns than brains
shotguns = 0
        brains = 0
        while brains>shotguns:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            
            diceRollResults = zombiedice.roll()


'''