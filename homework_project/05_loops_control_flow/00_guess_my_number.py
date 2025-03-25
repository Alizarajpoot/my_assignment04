import random

def main():
    # Generate the secret number randomly between 0 and 99
    secret_number = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")
    
    while True:
        # Get user's guess
        try:
            guess = int(input("Enter a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break  # Exit loop when the correct number is guessed

if __name__ == '__main__':
    main()
