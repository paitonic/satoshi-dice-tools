import random

max_roll = 65535

def roll():
    return random.randint(0, max_roll)

def calc_probability(less_then_target):
    win_probability = float(less_then_target) / (max_roll + 1) * 100
    return win_probability

def payout(bet_amount, less_then_target):
    return (bet_amount * (max_roll+1) / float(less_then_target)) * (100 - 1.9) / 100

def payout_multiplier(less_then_target):
    return (max_roll+1) / float(less_then_target) * (100 - 1.9) / 100

def profit(bet_amount, less_then_target):
    return payout(bet_amount, less_then_target) - bet_amount

def flat_bet_strategy():
    starting_balance = 0.00010000
    max_balance = starting_balance
    balance = starting_balance
    bet_amount = 0.00000100

    # max target = 64225
    less_then_target = 230

    for round in xrange(0, 1000000):
        # roll the dice
        dice = roll()

        # exit on negative balance
        if (balance - bet_amount < 0):
            break

        # substract bet amount
        balance -= bet_amount

        # if dice is lower, we get the payment
        if less_then_target > dice:
            balance += payout(bet_amount, less_then_target)
            if balance > max_balance:
                max_balance = balance
            outcome = "outcome=+{outcome:.8f}".format(outcome=profit(bet_amount, less_then_target))
        else:
            outcome = "outcome=-{outcome:.8f}".format(outcome=bet_amount)

        print "round={round} dice={dice:<5} bet={bet:.8f} {outcome} balance={balance:.8f}".format(
        round=round,
        dice=dice,
        target=less_then_target,
        outcome=outcome,
        bet=bet_amount,
        balance=balance)

    # stats
    print "target={target} probability={win:.3f}% starting_balance={starting_balance:.8f} balance={balance:.8f} max_balance={max_balance:.8f} payout=x{payout:.5f}\n".format(
    target=less_then_target,
    win=calc_probability(less_then_target),
    starting_balance=starting_balance,
    balance=balance,
    max_balance=max_balance,
    payout=payout_multiplier(less_then_target))

flat_bet_strategy()
