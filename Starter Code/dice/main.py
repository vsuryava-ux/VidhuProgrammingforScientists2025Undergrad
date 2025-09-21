"""
Pseudocode (from Learning Objectives)

RollDie()
    roll ← RandIntn(6)
    return roll + 1

PlayCrapsOnce()
    numDice ← 2
    firstRoll ← SumDice(numDice)
    if firstRoll = 2, 3, or 12
        return false (player loses)
    else if firstRoll = 7 or 11
        return true (player wins)
    else
        while true
            newRoll ← SumDice(numDice)
            if newRoll = firstRoll 
               return true
            else if newRoll = 7
                return false

ComputeCrapsHouseEdge(numTrials)
    count ← 0
    for numTrials total trials
        outcome ← PlayCrapsOnce()
        if outcome = true
            count ← count + 1
        else
            count ← count − 1
    return count/numTrials

Built-in PRNG references
- RandIntn(n)  → Python: random.randrange(a, b) returns integer in [a, b-1]
- RandFloat()  → Python: random.random() returns float in [0, 1)
"""

import random


def roll_die() -> int:
    """
    Simulates the roll of a die.
    Returns:
    - int: A pseudorandom integer between 1 and 6, inclusively.
    """
    return random.randrange(1, 7)


def sum_dice(num_dice: int) -> int:
    """
    Simulates the process of summing n dice.
    Parameters:
    - num_dice (int): The number of dice to sum.
    Returns:
    - int: The sum of num_dice simulated dice.
    """
    if num_dice <= 0:
        raise ValueError("num_dice must be a positive integer.")

    summed_dice_roll = 0

    for i in range(1, num_dice + 1):
        summed_dice_roll += roll_die()

    return summed_dice_roll


def play_craps_once() -> bool:
    """
    Simulates one game of craps.
    Returns:
    - bool: True if the game is a win, False if it's a loss.
    """
    first_roll = sum_dice(2)
    # did we win?
    if first_roll == 7 or first_roll == 11:
        return True  # win
    elif first_roll == 2 or first_roll == 3 or first_roll == 12:
        return False
    else:
        # first_roll is a winner and 7 is a loser
        while True:
            new_roll = sum_dice(2)
            # is the new roll seven or the previous roll's value
            if new_roll  == first_roll:
                return True  # win
            elif new_roll == 7:
                return False
            # else keep rolling, so start over


def compute_craps_house_edge(num_trials: int) -> float:
    """
    Estimates the "house edge" of craps over multiple simulations.
    Parameters:
    - num_trials (int): The number of simulations.
    Returns:
    - float: The house edge of craps (average amount won or lost per game, per unit bet).
    Positive means player profit; negative means house profit.
    """
    if num_trials <= 0:
        raise ValueError("num_trials must be a positive integer.")
    
    count = 0  # winnings/losings

    for i in range(0, num_trials):  # run trials of the game and keep track of winnings
        outcome = play_craps_once()
        if outcome:  # win
            count += 1
        else:
            count -= 1

    return count / num_trials  # average outcome over all trials, which is the house edge






def first_turn_craps() -> int:
    """
    This function essentially simulates the first turn of a game of craps through rolling two die at random.
    """

    return sum_dice(2)  # calls upon subroutines to randomly roll 2 die and sum them to essentially simulate the first turn of craps


def estimate_first_roll_win(num_trials: int) -> float:
    """
    This function will take in an integer representing the number of times we will play a game of craps. The function will return a float representing the probability that the player wins on the first roll.

    num_trials: number of times we play the game

    Returns: the probability that we win on the first try over num_trials times played
    """
    if num_trials <= 0:
        return 0  # we have no chance of winning if we do not play
    
    first_turn_win_count = 0  # this is a counter variable that keeps track of how many times we win in our first turn over num_trials

    for i in range(0, num_trials):
        if first_turn_craps() == 7 or first_turn_craps() == 11:  # simulates the first turn of craps, if the player wins, we increment the counter variable
            first_turn_win_count += 1
        # if the player loses, we just restart the loop to move on to the second time we play
    
    return first_turn_win_count / num_trials  # the probability that we win on the first turn over num_trials tries would be the number of times we won over the number of tries



def play_craps_dicerolls() -> int:
    """
    Simulates one game of craps. And just returns the number of dice rolls in the game as soon as the game ends. For this daily challenge we actually do not need information about whether they won or lost.

    Returns: integer value representing the number of dice rolls in that game.
    """
    roll_num = 0

    first_roll = sum_dice(2)
    roll_num += 1  # this essentially increments the roll_num variable every time we call the sum_dice function because this is when we roll dice
    # did we win?
    if first_roll == 7 or first_roll == 11:
        return roll_num  # win
    elif first_roll == 2 or first_roll == 3 or first_roll == 12:
        return roll_num  # as soon as we hit a game ending state, we just return the current value of roll_num
    else:
        # first_roll is a winner and 7 is a loser
        while True:
            new_roll = sum_dice(2)
            roll_num += 1
            # is the new roll seven or the previous roll's value
            if new_roll  == first_roll:
                return roll_num  # win
            elif new_roll == 7:
                return roll_num
            # else keep rolling, so start over





def averge_game_length(num_trials: int) -> float:
    """
    This simulates num_trials games of craps and estimates the average number of dice rolls per game.

    num_trials: integer input representing the number of times we play craps

    Returns: float representing the average number of dice rolls per game. total_dice_rolls / num_trials
    """
    if num_trials <= 0:
        return 0  # zero rolls per game if you do not play the game
    
    total_dice_rolls = 0  # initializes the total number of dice rolls

    for i in range(0, num_trials):
        total_dice_rolls += play_craps_dicerolls()  # each time we play we add the number of dice rolls that game had to the total_dice_rolls

    return total_dice_rolls / num_trials  # computes average dice rolls per game



def main():
    print("Rolling dice and playing craps.")

    num_trials = 1000

    edge = compute_craps_house_edge(num_trials)

    print(f"Estimated house edge with {num_trials} trials is: {edge:.6f}")


    random.seed(0)  # this seeds the PRNG with an arbitrary value, remember all PRNGs must start with seeds and the random number generation is the numbers produced when we do operations on that seed. Usually seeding with 0 will not produce random numbers, so python has started to seed random number generators based on the current time

    random.randint(0, 10)  # this outputs integer between 0 and 10 inclusively

    random.randrange(0, 10)  # this ouputs an integer between 0 and 9, inclusively

    random.random()  # prints decimal in range [0, 1)





if __name__ == "__main__":
    main()
