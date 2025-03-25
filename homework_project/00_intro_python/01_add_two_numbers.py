#Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:
#Prompt the user to enter the first number.
#Read the input and convert it to an integer.
#Prompt the user to enter the second number.
#Read the input and convert it to an integer.
#Calculate the sum of the two numbers.
#Print the total sum with an appropriate message.
#The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.

def main():
    print("This program adds two numbers.")
    
    # Prompt user for input
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Calculate the sum
    total = num1 + num2

    # Display the result
    print(f"The total is {total}.")  # Using f-string for cleaner formatting


# Required line to call the main function
if __name__ == '__main__':
    main()
