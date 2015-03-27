import random
from satoshidicetools.simulator import satoshidice

"""
Change less_then value every round.
"""

class Randomizer(satoshidice.Simulator):
    def strategy(self, previous_bet):
        self.less_then = random.randint(1, 64225)

    def on_strategy_end(self):
        self.plot()

randomizer = Randomizer(balance=0.0001, bet_amount=0.000001, less_then=49152)
randomizer.run()
