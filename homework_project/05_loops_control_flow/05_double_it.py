def main():
    # Get user input and convert to an integer
    curr_value = int(input("Enter a number: "))

    # Loop until curr_value is 100 or greater
    while curr_value < 100:
        curr_value *= 2  # Double the value
        print(curr_value)  # Print the doubled value

# Call the main function when the script runs
if __name__ == "__main__":
    main()
