from satoshidicetools.simulator import satoshidice

"""
(source: investopedia)
An anti-Martingale strategy involves halving your bets each time you lose a trade, and doubling them each time you win a trade.
"""

class AntiMartingale(satoshidice.Simulator):
    def on_strategy_start(self):
        self.outcomes = []

    def strategy(self, previous_bet):
        if previous_bet:
            is_won = True if (previous_bet['profit'] > 0) else False
        else:
            return
        
        if is_won:
            self.bet_amount = self.bet_amount * 2
        else:
            self.bet_amount = self.bet_amount / 2

    def on_strategy_end(self):
        self.plot()

antimartingale = AntiMartingale(balance=0.001, bet_amount=0.00001, less_then=44957)
antimartingale.run()
