from satoshidicetools.simulator import satoshidice

"""
On streak loss increase less_then value on streak win decrease less_then value.
"""

class LessThenMultiply(satoshidice.Simulator):
    def on_strategy_start(self):
        self.outcomes = []

    def strategy(self, previous_bet):
        if previous_bet:
            is_won = True if (previous_bet['profit'] > 0) else False
            self.outcomes.append(is_won)

        # streak loss
        if all([x == False for x in self.outcomes[-3:]]) and self.less_then * 1.3 < satoshidice.MAX_ROLL_TARGET:
            self.less_then = int(self.less_then * 1.3)
        elif all([x for x in self.outcomes[-3:]]) and self.less_then * 0.9 > satoshidice.MIN_ROLL_TARGET:
            self.less_then = int(self.less_then * 0.9)

    def on_strategy_end(self):
        self.plot()

lessthenmultiply = LessThenMultiply(balance=0.001, bet_amount=0.00001, less_then=32200)
lessthenmultiply.run()
