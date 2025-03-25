def main():
    lst = []  # Create an empty list

    val = input("Enter a value: ")  # Prompt the user for input
    while val:  # Continue as long as input is not empty
        lst.append(val)  # Add value to the list
        val = input("Enter a value: ")  # Get the next value

    print("Here's the list:", lst)  # Print the final list


if __name__ == '__main__':
    main()
