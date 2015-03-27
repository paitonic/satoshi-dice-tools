from satoshidicetools.simulator import satoshidice

"""
Change less_then value to %5 above it's average.
"""

class Average(satoshidice.Simulator):
    def on_strategy_start(self):
        self.less_then_values = []
        self.less_then_average = 0
        self.rounds = 0

    def strategy(self, previous_bet):
        self.rounds += 1
        if previous_bet:
            self.less_then_values.append(previous_bet['dice'])
            self.less_then_average = int(sum(self.less_then_values) / self.rounds)

        # 3 rounds warmup
        if (self.less_then_average > 0 and self.rounds > 3):
            self.less_then = int(self.less_then_average * 1.05)

    def on_strategy_end(self):
        self.plot()

average = Average(balance=0.001, bet_amount=0.0001, less_then=32200)
average.run()
