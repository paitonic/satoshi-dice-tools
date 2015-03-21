from satoshidicetools.simulator import satoshidice

class Flatbet(satoshidice.Simulator):
    def strategy(selef, previous_bet):
        pass
    
    def on_strategy_end(self):
        self.plot()


flatbet = Flatbet(balance=0.001, bet_amount=0.0001, less_then=45000)
flatbet.run()
