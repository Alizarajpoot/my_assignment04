#Ask the user for a number and print its square (the product of the number times itself).
#Here's a sample run of the program (user input is in bold italics):
#Type a number to see its square: 4
#4.0 squared is 16.0

def main():
    # Ask the user for a number
    num = float(input("Type a number to see its square: "))

    # Calculate the square
    square = num ** 2

    # Print the result using f-string for better readability
    print(f"{num} squared is {square}")


# Required line to call the main function
if __name__ == '__main__':
    main()
