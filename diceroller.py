import datetime
from satoshidice import SatoshiDiceApi

class DiceRoller:
    """
    DiceRoller bot skeleton.
    """

    def __init__(self, secret):
        self.api = SatoshiDiceApi(secret=secret)

    def bet(self, bet_in_satoshis, below_roll_to_win, client_roll):
        result = self.api.place_bet(bet_in_satoshis, below_roll_to_win, client_roll)
        self.output_bet_info(result)

    def output_bet_info(self, result):
        print "{date}:".format(date=datetime.datetime.now())
        print "bet={bet:.8f} payout={payout:.8f} profit={profit:.8f} balance={balance:.8f} outcome={outcome} probability={probability}% target={target} roll={roll}".format(
        bet=result["bet"]["betInSatoshis"],
        payout=result["bet"]["payoutInSatoshis"],
        profit=result["bet"]["profitInSatoshis"],
        balance=result["userBalanceInSatoshis"],
        probability=result["bet"]["probability"],
        target=result["bet"]["target"],
        roll=result["bet"]["roll"],
        outcome=result["bet"]["result"])
        print "\n"
