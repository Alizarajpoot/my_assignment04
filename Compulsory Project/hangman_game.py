
#project 5
import random

# List of words
words = ["enum", "vscode", "python", "colab", "game"]
word = random.choice(words)  # Select a random word

guessed_letters = []
attempts = 6

print("Welcome to the Hangman Project!")
print("_" * len(word))  # Display blanks for the word

while attempts > 0:
    guess = input("\n Guess a letter: ").lower()

    # Check if input is a single alphabet
    if len(guess) != 1 or not guess.isalpha():
        print("Write only one letter!")
        continue

    # Check if letter is already guessed
    if guess in guessed_letters:
        print("This letter is already chosen, try another letter.")
        continue

    # Add guessed letter to the list
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print(f"Wrong! {attempts} attempts left.")

    # Display current word progress
    displayed_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
    print(displayed_word)

    # Check if the player has guessed the word
    if "_" not in displayed_word:
        print(f"🎉 Congratulations! You guessed the word: {word}")
        break