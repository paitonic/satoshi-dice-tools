import random

max_roll = 65535

def roll():
    """
    Roll the dice.
    Note: this is simplified approach using random.randint()
    """
    return random.randint(0, max_roll)

def probability(less_then_target):
    """
    Calculate win chance, returns float, for example 90.15.
    """
    return float(less_then_target) / (max_roll + 1) * 100

def payout(bet_amount, less_then_target, dice):
    """
    Function returns payout (in BTC) based on given bet amount (in BTC), target and roll result.
    """
    if (less_then_target > dice):
        return (bet_amount * (max_roll+1) / float(less_then_target)) * (100 - 1.9) / 100
    else:
        return 0

def payout_multiplier(less_then_target):
    """
    Function returns payout multiplier for given target, for example, target 32768 has 1.962 multplier.
    """
    house_edge = 1.9
    return (max_roll+1) / float(less_then_target) * (100 - house_edge) / 100

def profit(bet_amount, less_then_target, dice):
    """
    Function returns profit or loss (in BTC) after rolling the dice.
    Expects bet amount, target and dice result.
    """
    if (less_then_target > dice):
        return payout(bet_amount, less_then_target, dice) - bet_amount
    else:
        return -bet_amount

def round_stats(*args, **kwargs):
    """
    Stats after one round is finished.
    """
    print "round={round} dice={dice:<5} bet={bet:.8f} profit={profit:+.8f} chance={win:.3f}% payout=x{payout:.5f} balance={balance:.8f}".format(
        round=kwargs['round_id'],
        dice=kwargs['dice'],
        target=kwargs['target'],
        profit=kwargs['profit'],
        bet=kwargs['bet_amount'],
        balance=kwargs['balance'],
        win=probability(kwargs['target']),
        payout=payout_multiplier(kwargs['target']))

def overall_stats(*args, **kwargs):
    """
    Stats after all rounds of betting are finished.
    """
    max_balance_percent = kwargs['max_balance'] / kwargs['starting_balance'] * 100
    rounds_won_percent = kwargs['rounds_won'] / float(kwargs['rounds_won'] + kwargs['rounds_lost']) * 100
    rounds_lost_percent = kwargs['rounds_lost'] / float(kwargs['rounds_won'] + kwargs['rounds_lost']) * 100
    print "starting_balance={starting_balance:.8f} max_balance={max_balance:.8f}/{max_balance_percent:.2f}% rounds_won={rounds_won}/{rounds_won_percentage:.2f}% rounds_lost={rounds_lost}/{rounds_lost_percentage:.2f}%".format(
        starting_balance=kwargs['starting_balance'],
        max_balance=kwargs['max_balance'],
        rounds_won=kwargs['rounds_won'],
        rounds_lost=kwargs['rounds_lost'],
        max_balance_percent= max_balance_percent,
        rounds_won_percentage = rounds_won_percent,
        rounds_lost_percentage = rounds_lost_percent)
