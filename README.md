# satoshi-dice-roller
Utility for interacting with satoshidice.com API, strategy simulator and example of few strategies.

##### API
```satoshidice.py``` supports very basic API functionality.

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
