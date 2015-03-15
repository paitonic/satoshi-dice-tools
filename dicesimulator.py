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
