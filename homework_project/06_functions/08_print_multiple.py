def print_multiple(message: str, repeats: int):
    """Prints the given message multiple times based on the repeats value."""
    for _ in range(repeats):
        print(message)

def main():
    message = input("Please type a message: ")
    
    try:
        repeats = int(input("Enter a number of times to repeat your message: "))
        print_multiple(message, repeats)
    except ValueError:
        print("Invalid input! Please enter a valid integer for the number of repeats.")

if __name__ == '__main__':
    main()
