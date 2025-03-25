#number gaame user project 3
import random
print("guess the number between 1 and 100!")
number=random.randint(1,100)

while True:
  guess=int(input("enter your guess number:"))
  if guess < number:
    print("to low number!")
  elif guess > number:
      print("to high number!")
  else:
        print("congrats you got it right!")
        break