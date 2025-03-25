ADULT_AGE = 18  # U.S. legal adult age

def is_adult(age: int) -> bool:
    """
    Returns True if age is greater than or equal to ADULT_AGE, otherwise False.
    """
    return age >= ADULT_AGE

def main():
    age = int(input("How old is this person?: "))  # Get user input and convert to integer
    print(is_adult(age))  # Print the result of the is_adult function

if __name__ == "__main__":
    main()
