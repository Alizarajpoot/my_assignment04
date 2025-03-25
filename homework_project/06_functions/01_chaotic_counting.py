import random

DONE_LIKELIHOOD = 0.3  # Adjust probability as needed

def chaotic_counting():
    for num in range(1, 11):  # Count from 1 to 10
        if done():
            return  # Stops execution and returns to main()
        print(num)

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    return random.random() < DONE_LIKELIHOOD

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()
