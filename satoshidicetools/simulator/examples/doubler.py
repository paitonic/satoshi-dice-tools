from satoshidicetools.simulator import satoshidice

"""
Double every bet.
"""

class Doubler(satoshidice.Simulator):
    def on_strategy_start(self):
        self.outcomes = []

    def strategy(self, previous_bet):
        self.bet_amount = self.bet_amount * 2

    def on_strategy_end(self):
        self.plot()

doubler = Doubler(balance=0.001, bet_amount=0.00001, less_then=32112)
doubler.run()
