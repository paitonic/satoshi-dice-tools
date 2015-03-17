import dicesimulator
import random

class Randomizer(dicesimulator.DiceSimulator):
    def strategy(self, previous_bet):
        self.less_then = random.randint(1, 64225)

randomizer = Randomizer(balance=0.0001, bet_amount=0.000001, less_then=49152)
randomizer.run()
