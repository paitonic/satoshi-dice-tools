import dicesimulator

"""
Example of simple strategy based on mistaken belief (Gambler's Fallacy).
http://vegasclick.com/gambling/fallacy.html
http://en.wikipedia.org/wiki/Gambler%27s_fallacy

In this strategy we bet that our target will be less 49152 (75% prob.).
In addition, if past 3 rolls were higher than 32768 (50% prob.) we will switch to 32768 target and wait
until we hit it.
"""

starting_balance = 0.00100000
max_balance = starting_balance
balance = starting_balance
bet_amount = 0.00010000
past_roll_results = [] # 1 win, 0 loss

rounds_won = 0
rounds_lost = 0
round_id = 0
while (balance - bet_amount > 0):
    # are we got 3 losses streak?
    if (len(past_roll_results) > 3) and (all(i == 0 for i in past_roll_results[-3:])):
        # increase risk, 50% - x1.96200
        less_then_target = 32768
    else:
        # decrease risk, 49152 - 75% - x1.3080
        less_then_target = 49152

    round_id += 1

    # roll the dice
    dice = dicesimulator.roll()

    # substract bet amount
    balance -= bet_amount

    # receive payout
    balance += dicesimulator.payout(bet_amount, less_then_target, dice)

    # keep track of max balance
    if balance > max_balance:
        max_balance = balance

    # profit/loss made
    profit = dicesimulator.profit(bet_amount, less_then_target, dice)

    if profit > 0:
        past_roll_results.append(1)
        rounds_won += 1
    else:
        past_roll_results.append(0)
        rounds_lost += 1

    dicesimulator.round_stats(round_id=round_id, dice=dice, target=less_then_target, profit=profit, bet_amount=bet_amount, balance=balance)

dicesimulator.overall_stats(starting_balance=starting_balance, max_balance=max_balance, rounds_won=rounds_won, rounds_lost=rounds_lost)
