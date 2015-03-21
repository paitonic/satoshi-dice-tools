from satoshidicetools.simulator import satoshidice

class Flatbet(satoshidice.Simulator):
    def strategy(self, previous_bet):
        pass

flatbet = Flatbet(balance=0.001, bet_amount=0.0001, less_then=45000)
flatbet.run()
