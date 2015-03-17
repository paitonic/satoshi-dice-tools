# satoshi-dice-roller
Utility for interacting with satoshidice.com API, strategy simulator and example of few strategies.

##### API
```satoshidice.py``` supports very basic API functionality.

```python
from satoshidice import SatoshiDiceApi
api = SatoshiDiceApi(secret="SECRET_HASH")
```

Balance:
```python
api.balance()
```
```json
{u'balanceInSatoshis': 1000001,
 u'hash': u'hash',
 u'maxProfitInSatoshis': 583281011,
 u'nick': u'wowa',
 u'queryTimeInSeconds': 0.1765,
 u'unconfirmedBalanceInsSatoshis': 0}
```

Let's place new bet for 1000 satoshi (0.00001000 BTC) and target of 62,000:
```python
bet = api.place_bet(1000, 62000)
```
```
{u'bet': {u'betID': 00000000,
  u'betInSatoshis': 1000,
  u'betTX': None,
  u'betType': u'lessthan',
  u'game': u'session',
  u'payoutInSatoshis': 1036,
  u'payoutTX': None,
  u'playerHash': u'00000000',
  u'playerNick': u'0000',
  u'prize': u'x1.036',
  u'prizeInSatoshis': 1036,
  u'probability': u'94.6',
  u'profitInSatoshis': 36,
  u'result': u'win',
  u'roll': 4977,
  u'rollInPercent': u'7.59',
  u'streak': 1,
  u'streakBetInSatoshis': 1000,
  u'streakProbability': 0.946044921875,
  u'streakWinInSatoshis': 1036,
  u'target': 62000,
  u'time': u'2015-03-17 07:49:51'},
 u'clientRoll': 0,
 u'message': u'WIN! 7.59/94.6% +0.00000036',
 u'newLuck': 1.0026457060496,
 u'newLuckToday': 1.0570322580645,
 u'nextRound': {u'hash': 00000000',
  u'id': 13356925,
  u'maxProfitInSatoshis': 583275960,
  u'welcomeMessage': u''},
 u'queryTimeInSeconds': 1.5361180305481,
 u'resultingRoll': 4977,
 u'serverHash': u'00000000',
 u'serverRoll': 4977,
 u'serverSalt': u'00000000',
 u'status': u'success',
 u'userBalanceInSatoshis': 1000037}

```

##### Utility Functions for Strategy Testing
```dicesimulator.py``` includes several utility functions for testing your strategies locally without wasting even one satoshi!

For "rolling the dice" I used ```random.randint()``` instead of implementing the actual algorithm behind (I know, lazy me).

##### Bot Skeleton
```diceroller.py``` includes just a template for bot, nothing special.

##### Example of Strategies
Also, you can find few strategies (```*strategy.py``` files) I have implemented as an examples.
I warn you, none of those strategies are profitable and they were made for fun.

Output:

```
$ python flatbetstrategy.py

round=1 dice=34931 bet=0.00000100 profit=-0.00000100 chance=0.351% payout=x279.52529 balance=0.00009900
round=2 dice=58276 bet=0.00000100 profit=-0.00000100 chance=0.351% payout=x279.52529 balance=0.00009800
round=3 dice=10740 bet=0.00000100 profit=-0.00000100 chance=0.351% payout=x279.52529 balance=0.00009700
round=4 dice=62963 bet=0.00000100 profit=-0.00000100 chance=0.351% payout=x279.52529 balance=0.00009600
round=5 dice=56967 bet=0.00000100 profit=-0.00000100 chance=0.351% payout=x279.52529 balance=0.00009500
```

By the way, I'm not responsible for your losses or profits :).
