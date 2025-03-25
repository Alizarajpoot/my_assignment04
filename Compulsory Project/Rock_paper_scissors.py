#project 4

import random
# Game choices
choices = ["rock", "paper", "scissors"]

# Player choice
player_choice = input("Enter rock, paper, or scissors: ").lower()

# Validate player input
if player_choice not in choices:
    print("Invalid choice! Please choose rock, paper, or scissors.")
else:
    # Computer choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Winner decision
    if player_choice == computer_choice:
        print(f"Both chose {player_choice}. It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print(f"Player wins! {player_choice} beats {computer_choice}.")
    else:
        print(f"Computer wins! {computer_choice} beats {player_choice}.")
