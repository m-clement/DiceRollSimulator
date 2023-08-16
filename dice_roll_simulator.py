import random

def roll_dice():
    """Simulate the rolling of two dice and display the result with visual representations."""
    
    # Visual representations for dice faces 1 through 6
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

    # Prompt the user to decide if they want to roll the dice
    roll = input("Roll the dice? (y/n): ")

    # Continue rolling until the user decides to stop
    while roll.lower() == "y".lower():
        # Randomly determine the values of the two dice
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        # Display the rolled values and their visual representations
        print("Dice rolled:\n{} and {}".format(die1, die2))
        print("\n".join(dice_drawing[die1]))
        print("\n".join(dice_drawing[die2]))

        # Ask the user if they want to roll the dice again
        roll = input("Roll again? (y/n): ")

# Execute the dice rolling function
if __name__ == "__main__":
    roll_dice()
