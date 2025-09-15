"""
Pseudocode (from Learning Objectives)

RollDie()
    roll ← RandIntn(6)
    return roll + 1

Built-in PRNG references
- RandIntn(n)  → Python: random.randrange(a, b) returns integer in [a, b-1]
- RandFloat()  → Python: random.random() returns float in [0, 1)
"""

import random

def main():
    print("Rolling dice and playing craps.")
    # (Optional) deterministic testing:
    # random.seed(0)

    # (Optional) quick demos:
    # print(random.randrange(0, 10))  # integer in [0, 9]
    # print(random.random())          # float in [0, 1)
    # for _ in range(10):
    #     print("Die roll:", roll_die())
    # for _ in range(10):
    #     print("Two-dice sum:", sum_dice(2))


def roll_die() -> int:
    """
    Simulates the roll of a die.
    Returns:
    - int: A pseudorandom integer between 1 and 6, inclusively.
    """
    return random.randrange(1, 7)


def sum_two_dice() -> int:
    """
    Simulates the sum of two dice.
    Returns:
    - int: The simulated sum of two dice (between 2 and 12).
    """
    return roll_die() + roll_die()


def sum_dice(num_dice: int) -> int:
    """
    Simulates the process of summing n dice.
    Parameters:
    - num_dice (int): The number of dice to sum.
    Returns:
    - int: The sum of num_dice simulated dice.
    """
    total = 0
    for _ in range(num_dice):
        total += roll_die()
    return total


if __name__ == "__main__":
    main()
