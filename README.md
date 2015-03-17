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

#### DiceSimulator for Strategy Testing
```DiceSimulator``` class contains several utility methods for testing your strategies locally without wasting even one satoshi!


##### Writing strategy
First of all we have to import ```dicesimulator```

```python
import dicesimulator
```

Now let's implement [Martingale](http://en.wikipedia.org/wiki/Martingale_%28betting_system%29).

Every strategy should inherit ```dicesimulator.DiceSimulator``` class and implement ```strategy()``` method which expects ```previous_bet``` object that contains your result of previous bet, you can use this object if your strategy needs access to previous bet results each round.

```python
class Martingale(dicesimulator.DiceSimulator):
    def strategy(self, previous_bet):
      if previous_bet and previous_bet['profit'] < 0:
          # if previous bet was a loss then double bet amount
          self.bet_amount = previous_bet['bet_amount'] * 2
      else:
          # else set initial amount
          self.bet_amount = self.initial_bet_amount
```
```DiceSimulator``` class have number of properties you can change or read.
For example, to change bet amount simply assign new bet to ```self.bet_amount``` property, if you want access to initial bet amount then there is ```self.initial_bet_amount```, same thing for less_then and balance properties.

Almost done, lets create object with initial configuration
```python
martingale = Martingale(balance=0.001, bet_amount=0.00001, less_then=32768)
```

Finally, call objects ```.run()``` method to begin the simulation loop, in each iteration ```strategy()``` function will be called to "handle" the round/roll.
Simulation will run until your all of your balance is lost :).
```python
martingale.run()
```

> **Note:**
for "rolling the dice", ```random.randint()``` was used instead of implementing the actual algorithm behind (I know, lazy me).

Here's how output looks like:

```
$ python martingalestrategy.py

round=1374 dice=11726 less_then=5657  bet=0.00000100 profit=-0.00000100 chance=8.632% payout=x11.36483 balance=0.00000160
round=1375 dice=51523 less_then=7240  bet=0.00000100 profit=-0.00000100 chance=11.047% payout=x8.87995 balance=0.00000060
round=1376 dice=53891 less_then=12293 bet=0.00000100 profit=-0.00000100 chance=18.758% payout=x5.22987 balance=-0.00000040
initial_balance=0.00010000 max_balance=0.00010425/104.25% rounds_won=665/48.33% rounds_lost=711/51.67%
```

###### Example of Strategies
You can find some examples of genius (oh, yes!) strategies (look for ```*strategy.py``` files).
None of those strategies are profitable and they were made for fun just like this entire project :).

##### Bot Skeleton
```diceroller.py``` includes just a template for bot, nothing special.



By the way, I'm not responsible for your losses or profits :).
