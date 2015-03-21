import random

MAX_ROLL = 65535 # maximum roll
MAX_ROLL_TARGET = 64225 # max target
HOUSE_EDGE = 1.9

class Simulator:
    def __init__(self, balance, bet_amount=0.1, less_then=1):
        self.initial_balance = self.max_balance = self.balance = self.cumulative_balance = balance
        self.initial_bet_amount = self.bet_amount = bet_amount
        self.initial_less_then = self.less_then = less_then
        self.custom_round_output_string = ''

    def reset_state(self):
        """
        Set initial values.
        """
        self.max_balance = self.balance = self.cumulative_balance = self.initial_balance
        self.bet_amount = self.initial_bet_amount
        self.less_then = self.initial_less_then
        self.custom_round_output_string = ''

    def roll(self):
        """
        Roll the dice.
        Note: this is simplified approach using random.randint()
        """
        return random.randint(0, MAX_ROLL)

    def probability(self, less_then):
        """
        Calculate win chance, returns float, for example 90.15.
        """
        return float(less_then) / (MAX_ROLL + 1) * 100

    def payout(self, bet_amount, less_then, dice):
        """
        Function returns payout (in BTC) based on given bet amount (in BTC), target and roll result.
        """
        if (less_then > dice):
            return (bet_amount * (MAX_ROLL+1) / float(less_then)) * (100 - 1.9) / 100
        else:
            return 0

    def payout_multiplier(self, less_then):
        """
        Function returns payout multiplier for given target, for example, target 32768 has 1.962 multplier.
        """
        return (MAX_ROLL+1) / float(less_then) * (100 - HOUSE_EDGE) / 100

    def calculate_profit(self, bet_amount, less_then, dice):
        """
        Function returns profit or loss (in BTC) after rolling the dice.
        Expects bet amount, target and dice result.
        """
        if (less_then > dice):
            return self.payout(bet_amount, less_then, dice) - bet_amount
        else:
            return -bet_amount

    def round_stats(self, round_id, bet_amount, less_then, dice, profit, custom_stat=''):
        """
        Stats after one round is finished.
        """
        print "round={round} dice={dice:<5} less_then={less_then:<5} bet={bet:.8f} profit={profit:+.8f} chance={win:.3f}% payout=x{payout:.5f} balance={balance:.8f} {custom_stat}".format(
            round=round_id,
            dice=dice,
            less_then=less_then,
            profit=profit,
            bet=bet_amount,
            balance=self.balance,
            win=self.probability(less_then),
            payout=self.payout_multiplier(less_then),
            custom_stat=self.custom_round_output_string)

    def overall_stats(self, rounds_won, rounds_lost):
        """
        Stats after all rounds of betting are finished.
        """
        max_balance_percent = self.max_balance / self.initial_balance * 100
        rounds_won_percent = rounds_won / float(rounds_won + rounds_lost) * 100
        rounds_lost_percent = rounds_lost / float(rounds_won + rounds_lost) * 100
        avg_balance = self.cumulative_balance /  (rounds_won + rounds_lost)

        print "initial_balance={initial_balance:.8f} max_balance={max_balance:.8f}/{max_balance_percent:.2f}% avg_balance={avg_balance:.8f} rounds_won={rounds_won}/{rounds_won_percentage:.2f}% rounds_lost={rounds_lost}/{rounds_lost_percentage:.2f}%".format(
            initial_balance=self.initial_balance,
            max_balance=self.max_balance,
            rounds_won=rounds_won,
            rounds_lost=rounds_lost,
            max_balance_percent=max_balance_percent,
            rounds_won_percentage=rounds_won_percent,
            rounds_lost_percentage=rounds_lost_percent,
            avg_balance=avg_balance)

    def add_to_round_output(self, output):
        """
        Add additional string of output after each round is complete.
        """
        self.custom_round_output_string = output

    def strategy_init(self):
        """
        Strategy initialization method (optional), use this method to initialize properties
        that should be accessable between rounds.
        """
        pass

    def strategy(self):
        """
        Strategy core, needs to be implemented by child class.
        """
        pass

    def is_strategy_stop(self):
        """
        Stop condition, this methods is called after self.strategy(), if your strategy has a termination condition - implement this method.
        """
        pass

    def on_strategy_end(self):
        """
        Do something after strategy finished running.
        """
        pass

    def run(self, iterations=1):
        """
        Strategy runner.
        """
        # iteration
        for iteration in xrange(0, iterations):
            self.strategy_init()
            previous_bet = None
            rounds_won = rounds_lost = 0
            round_id = 0

            # round
            while (self.balance > 0):
                round_id += 1
                dice = self.roll()

                # run strategy
                self.strategy(previous_bet)

                # check if strategy stop condition is met
                if self.is_strategy_stop():
                    break

                self.balance -= self.bet_amount
                outcome = self.payout(self.bet_amount, self.less_then, dice)
                self.balance += outcome
                self.cumulative_balance += self.balance

                # keep track of highest balance ever
                if self.balance > self.max_balance:
                    self.max_balance = self.balance

                profit = self.calculate_profit(self.bet_amount, self.less_then, dice)
                previous_bet = {'profit': profit, 'bet_amount': self.bet_amount, 'less_then': self.less_then, 'dice': dice, 'payout': outcome}

                # rounds won vs lost
                if profit > 0:
                    rounds_won += 1
                else:
                    rounds_lost += 1

                # if number of iterations is more than one
                # all statements below will be skipped
                if iterations > 1:
                    continue

                self.round_stats(round_id, self.bet_amount, self.less_then, dice, profit)

            self.overall_stats(rounds_won, rounds_lost)
            self.on_strategy_end()

            # reset configuration to initial state after each iteration
            self.reset_state()
