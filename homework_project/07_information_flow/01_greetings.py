def greet(name):
    """
    Takes a name as input and prints a greeting message.
    """
    print("Greetings", name + "!")

def main():
    name = input("What's your name? ")  # Get user's name
    greet(name)  # Call the greet function to print the greeting

if __name__ == '__main__':
    main()
