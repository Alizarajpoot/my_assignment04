#number guess project2 (computer)
import random
def guess_the_number():
  """ project 2 guess the number by computer."""
  number = random.randint(1, 100)
  guess_left =7

  #welcome massage
  print("welcome to the number gussing game")
  print("i am thinking of a number between 1 to 100")
  #loop generated
  while guess_left > 0:
    print(f"\nyou have {guess_left} guesses left")
    try:
      guess = int(input("take a guess of another number."))
    except ValueError:
      print("invalid input:please enter a number")
      continue
    #guess the secret number
    if guess < number:
      print("to low number . tell another!")
    elif guess > number:
      print("to hoigh number . tell another!")
    else:
      print(f"congratulations! you go the correct number in {7 - guess_left + 1} tries.")
      return
    guess_left -= 1
  #jab sub guess finish hu jay ge
  print(f"\nYou ran out of guesses. The number was {number}.")
guess_the_number()
