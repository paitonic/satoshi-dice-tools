import random

max_roll = 65535

def roll():
    return random.randint(0, max_roll)

def probability(less_then_target):
    return float(less_then_target) / (max_roll + 1) * 100

def payout(bet_amount, less_then_target, dice):
    if (less_then_target > dice):
        return (bet_amount * (max_roll+1) / float(less_then_target)) * (100 - 1.9) / 100
    else:
        return 0

def payout_multiplier(less_then_target):
    house_edge = 1.9
    return (max_roll+1) / float(less_then_target) * (100 - house_edge) / 100

def profit(bet_amount, less_then_target, dice):
    if (less_then_target > dice):
        return payout(bet_amount, less_then_target, dice) - bet_amount
    else:
        return -bet_amount
