def main():
    curr_value = int(input("Enter a number: "))  # Get user input as an integer

    while curr_value < 100:  # Continue looping while the number is less than 100
        curr_value *= 2  # Double the number
        print(curr_value, end=" ")  # Print the number on the same line with space

if __name__ == '__main__':
    main()
