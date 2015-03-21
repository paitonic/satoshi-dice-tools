from satoshidicetools.simulator import satoshidice

"""
http://vegasclick.com/gambling/fallacy.html
http://en.wikipedia.org/wiki/Gambler%27s_fallacy

In this strategy, we doing flat betting until we hit loss of 3 streak, once we got loss streak
we increase bet amount.
"""

class LikelyToHappen(satoshidice.Simulator):
    def strategy_init(self):
        # 0 - lost, 1 - won
        self.previous_outcomes = []

    def strategy(self, previous_bet):
        loss_streak = 3

        # keep track of out losses and profits
        if previous_bet:
            if previous_bet['profit'] > 0:
                self.previous_outcomes.append(1)
            else:
                self.previous_outcomes.append(0)

        # are we got loss streak?
        if (len(self.previous_outcomes) >= loss_streak) and (all(outcome == 0 for outcome in self.previous_outcomes[-loss_streak:])):
            # all in
            self.bet_amount = self.balance
        else:
            self.bet_amount = self.initial_bet_amount

likely_to_happen = LikelyToHappen(balance=0.001, bet_amount=0.0001, less_then=49152)
likely_to_happen.run()
