from satoshidicetools.simulator import satoshidice

"""
Mix between two less_then values
"""

class Mixbet(satoshidice.Simulator):
    def strategy(self, previous_bet):
        if (previous_bet and previous_bet['less_then'] == 44957):
            self.less_then = 57802
        else:
            self.less_then = 44957

    def on_strategy_end(self):
        self.plot()

flatbet = Mixbet(balance=0.001, bet_amount=0.0001, less_then=44957)
flatbet.run()
