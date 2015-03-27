# satoshi-dice-roller
Utility for interacting with satoshidice.com API and strategy simulator.


##### Package tree
```
satoshidicetools
├── api
│   ├── examples
│   │   └── diceroller.py
│   ├── __init__.py
│   ├── satoshidice.py
├── __init__.py
└── simulator
    ├── examples
    │   ├── antimartingale.py
    │   ├── average.py
    │   ├── doubler.py
    │   ├── flatbet.py
    │   ├── flat_tp_sl.py
    │   ├── lessthen_multiply.py
    │   ├── likelytohappen.py
    │   ├── martingale.py
    │   ├── minbalance.py
    │   ├── mix_less_then.py
    │   └── randomizer.py
    ├── __init__.py
    ├── satoshidice.py
```

##### API
```satoshidice.py``` supports very basic API functionality.

```python
from satoshidicetools.api import satoshidice
api = satoshidice.Api(secret="SECRET_HASH")
```

Balance:
```python
api.balance()
```
```python
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

```python
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

#### Simulator
```Simulator``` class contains several utility methods for testing your strategies locally without wasting even one satoshi!

Let's implement [Martingale](http://en.wikipedia.org/wiki/Martingale_%28betting_system%29).

Every strategy should inherit ```satoshidice.Simulator``` class and implement ```self.strategy()``` method which expects ```previous_bet``` dictionary that contains your result of previous bet, you can use this object if your strategy needs access to previous bet result each round.

```python
from satoshidicetools.simulator import satoshidice

class Martingale(dicesimulator.DiceSimulator):

    def on_strategy_start(self):
      """
      Do something before strategy is started running.
      """
      pass

    def stop_strategy_if(self):
      """
      End strategy running on some condition
      """
      pass

    def strategy(self, previous_bet):
      """
      Logic goes here.
      """
      if previous_bet and previous_bet['profit'] < 0:
          # if previous bet was a loss then double bet amount
          self.bet_amount = previous_bet['bet_amount'] * 2
      else:
          # else set initial amount
          self.bet_amount = self.initial_bet_amount

    def on_strategy_end(self):
      """
      do something when strategy finished running.
      """
      # lets our balance
      self.plot()
```

To change bet amount, simply assign new amount to ```self.bet_amount```, if you want access to initial bet amount then you can use ```self.initial_bet_amount```.

##### Additional properties:
  - ```self.max_balance``` - always contains the highest balance you were able to achieve.
  - ```self.initial_balance``` - initial balance
  - ```self.balance``` - current balance
  - ```self.initial_less_then``` - intial 'less then' value
  - ```self.less_then``` - current 'less then' value, can be changed.

Almost done, lets create object with initial configuration
```python
martingale = Martingale(balance=0.001, bet_amount=0.00001, less_then=32768)
```

Finally, call ```self.run()``` method to begin the simulation loop, in each iteration ```strategy()``` function will be called to "handle" the round/roll.
Simulation will run until your all of your balance is lost or when ```self.stop_strategy_if``` is returned ```True```.
```python
martingale.run()
```

In addition, you can specifiy if you want more than one iteration by passing ```iteration``` parameter to ```self.run()```.
```python
martingale.run(iterations=100)
```

> **Note:**
for "rolling the dice", ```random.randint()``` was used instead of implementing the actual algorithm behind (I know, lazy me).

Here's how output looks like:

```
$ python martingalestrategy.py
...
round=50 dice=64294 less_then=32112 bet=0.00008000 profit=-0.00008000 chance=48.999% payout=x2.00208 balance=0.00110158
round=51 dice=47772 less_then=32112 bet=0.00016000 profit=-0.00016000 chance=48.999% payout=x2.00208 balance=0.00094158
round=52 dice=46427 less_then=32112 bet=0.00032000 profit=-0.00032000 chance=48.999% payout=x2.00208 balance=0.00062158
initial_balance=0.00100000 balance=0.00062158 max_balance=0.00125158/125.16% avg_balance=0.00111207 rounds_won=25/48.08% rounds_lost=27/51.92%
```

Plot, red line is initial balance, the blue one is balance over time (after each roll/round is completed).

[![](http://i57.tinypic.com/2vi2ttu.png)](http://i57.tinypic.com/2vi2ttu.png)
> **Note:**
matplotlib is required for plotting.


You can find some examples of genius (oh yes!) strategies in ```satoshidicetools/simulator/examples``` directory.

None of those strategies are profitable and they were made for fun just like this entire project.
By the way, I'm not responsible for your losses or profits :).
