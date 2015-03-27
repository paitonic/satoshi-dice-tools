from satoshidicetools.simulator import satoshidice

"""
Flatbet variation. Uses stop loss and take profit.
"""

class Flatbet(satoshidice.Simulator):
    def strategy(selef, previous_bet):
        pass

    def on_strategy_end(self):
        self.plot()

    def stop_strategy_if(self):
        take_profit = self.initial_balance * 1.25
        stop_loss = self.initial_balance * 0.8

        if (self.balance >= take_profit) or (self.balance <= stop_loss):
            return True

flatbet = Flatbet(balance=0.001, bet_amount=0.0001, less_then=45000)
flatbet.run()
