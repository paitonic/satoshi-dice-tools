from satoshidicetools.simulator import satoshidice

"""
If our balance is lower than the initial,
    - decrease risk by increasing less_then value
    - increase bet amount
else:
    - set initial values
"""

class MinBalance(satoshidice.Simulator):
    def on_strategy_start(self):
        self.min_balance = self.initial_balance

    def strategy(self, previous_bet):
        if (self.balance < self.min_balance):
            self.min_balance = self.balance
            self.less_then = 58000
            self.bet_amount = self.balance * 0.7
        elif self.balance > (self.min_balance * 1.2):
            self.less_then = self.initial_less_then
            self.bet_amount = self.initial_bet_amount

    def on_strategy_end(self):
        self.plot()

minbalance = MinBalance(balance=0.001, bet_amount=0.0001, less_then=32400)
minbalance.run()
