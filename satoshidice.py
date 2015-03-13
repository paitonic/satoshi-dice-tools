import urllib
import json
import datetime

class SatoshiDiceApi:
    """
    Class for interacting with satoshidice.com API.
    """

    def __init__(self, secret):
        self.secret = secret
        self.api_base_url = "https://session.satoshidice.com/"
        self.next_round = {}

    def user_recent_rolls(self):
        response = urllib.urlopen(self.api_base_url + "globalstats/recentrolls/" + self.secret)
        return json.load(response)

    def balance(self):
        response = urllib.urlopen(self.api_base_url + "userapi/userbalance/?secret=" + self.secret)
        return json.load(response)

    def start_round(self):
        response = urllib.urlopen(self.api_base_url + "userapi/startround.php?secret=" + self.secret)
        self.next_round = json.load(response)

    def place_bet(self, bet_in_satoshis, below_roll_to_win, client_roll):
        # max/min allowed lucky numbers
        min_roll = 1
        max_roll = 64225

        if (below_roll_to_win < min_roll or below_roll_to_win > max_roll):
            print "{date} [error]: below_roll_to_win must be between {min_roll}-{max_roll} range".format(date=datetime.datetime.now(), max_roll=max_roll, min_roll=min_roll)
            return

        if self.next_round == {}:
            self.start_round()

        params = {
            'secret': self.secret,
            'betInSatoshis': bet_in_satoshis,
            'id': self.next_round['id'],
            'serverHash': self.next_round['hash'],
            'clientRoll': client_roll,
            'belowRollToWin': below_roll_to_win
        }

        # encode params
        params_encoded = urllib.urlencode(params)
        response = urllib.urlopen(self.api_base_url + 'userapi/placebet.php?' + params_encoded)

        # in case of failure
        response_json = json.load(response)
        if response_json["status"] == "fail":
            print "{date} [error]: Was unable to submit your bet".format(date=datetime.datetime.now())
            print "{date} [response]: {response}".format(date=datetime.datetime.now(), response=response_json)
            return

        # server returns nextRound object, on next bet we will use it instead
        # of making call to userapi/startround
        self.next_round = response_json['nextRound']

        return response_json
