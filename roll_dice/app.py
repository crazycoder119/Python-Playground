# ask user to roll the dice
# then use a random number
# use a dictionary to show the image or the random number
import random


def roll_dice():
    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),

    }
    roll = input('Are you sure? (y/n): ').lower().strip() == 'y'
    while roll:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1, 6)
        print("dice rolled: {} and {}".format(dice1,dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        roll = input('Are you sure? (y/n): ').lower().strip() == 'y'

roll_dice()