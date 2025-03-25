MINIMUM_HEIGHT = 50  # Minimum height required to ride

def main():
    height = float(input("How tall are you? "))  # Get user's height
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

# Run the main function
if __name__ == '__main__':
    main()
