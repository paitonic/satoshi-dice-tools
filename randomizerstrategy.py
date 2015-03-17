import dicesimulator
import random


# configuration
starting_balance = 0.00010000
max_balance = starting_balance
balance = starting_balance
bet_amount = 0.00000100
# less_then_target = 230 # max target = 64225

round_id = 0
rounds_won = 0
rounds_lost = 0

# while our balance is positive, let's roll!
while (balance - bet_amount > 0):
    round_id += 1

    # generate random target each round
    less_then_target = random.randint(1, 64225)

    # roll the dice
    dice = dicesimulator.roll()

    # substract bet amount from our balance
    balance -= bet_amount

    # add payout to our balance
    # payout can be positive (profit was made) or 0 (loss)
    # that's the amount that actually goes into our balance
    balance += dicesimulator.payout(bet_amount, less_then_target, dice)

    # let's track what maximum balance we
    # were able to get to
    if balance > max_balance:
        max_balance = balance

    # profit or loss amount
    profit = dicesimulator.profit(bet_amount, less_then_target, dice)
    if profit > 0:
        rounds_won += 1
    else:
        rounds_lost += 1

    # print some info after each roll
    dicesimulator.round_stats(round_id=round_id, dice=dice, target=less_then_target, profit=profit, bet_amount=bet_amount, balance=balance)

dicesimulator.overall_stats(starting_balance=starting_balance, max_balance=max_balance, rounds_won=rounds_won, rounds_lost=rounds_lost)
