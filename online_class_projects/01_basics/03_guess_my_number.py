import random

def main():
    # Generate a random number between 1 and 99
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")

    # Get the first guess from the user
    guess = int(input("Enter a guess: "))

    # Loop until the user guesses the correct number
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")

        # Prompt for a new guess
        guess = int(input("Enter a new number: "))

    # When guessed correctly, print a congratulatory message
    print(f"Congrats! The number was: {secret_number}")

# Run the game
if __name__ == '__main__':
    main()
