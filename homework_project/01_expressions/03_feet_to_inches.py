#Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

# Conversion factor: 1 foot = 12 inches
INCHES_IN_FOOT = 12  

def main():
    # Ask the user for the number of feet
    feet = float(input("Enter number of feet: "))

    # Convert feet to inches
    inches = feet * INCHES_IN_FOOT  

    # Display the result using f-strings
    print(f"That is {inches} inches!")


# Required line to call the main function
if __name__ == '__main__':
    main()