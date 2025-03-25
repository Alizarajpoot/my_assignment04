# Simulate rolling two dice, and prints results of each roll as well as the total.

import random  # Import the random module to simulate dice rolls

# Define the number of sides on each die
NUM_SIDES = 6

def main():
    # Roll the first and second die
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)

    # Calculate the total
    total = die1 + die2

    # Print the results
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

# Call the main function to execute the program
if __name__ == '__main__':
    main()
