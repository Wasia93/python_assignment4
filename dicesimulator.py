"""
Program: dice_simulator
-----------------------
Simulates rolling two dice, three times.
Prints the results of each die roll.
Demonstrates how variable scope works in Python.
"""

import random

# Constant for the number of sides on each die
NUM_SIDES = 6

def roll_dice():
    """Simulates rolling two dice and prints their individual values and total."""
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Die 1: {die1}, Die 2: {die2}, Total: {total}")

def main():
    # Local variable in main (not affected by roll_dice)
    die1 = 10
    print(f"die1 in main() starts as: {die1}")
    
    # Roll dice three times
    for i in range(3):
        print(f"\nRoll {i + 1}:")
        roll_dice()
    
    print(f"\ndie1 in main() is still: {die1}")

# Required to call main() when the script is run
if __name__ == '__main__':
    main()

