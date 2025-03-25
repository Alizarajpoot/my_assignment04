def print_divisors(num: int):
    """Prints all divisors of the given number."""
    print("Here are the divisors of", num)
    for i in range(1, num + 1):  # Start from 1, go up to num (inclusive)
        if num % i == 0:
            print(i)

def main():
    try:
        num = int(input("Enter a number: "))  # Get user input and convert to integer
        if num > 0:
            print_divisors(num)
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == '__main__':
    main()

