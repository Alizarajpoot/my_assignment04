def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create an empty phonebook

    while True:
        name = input("Name: ")
        if name == "":
            break  # Stop when the user enters an empty name
        number = input("Number: ")
        phonebook[name] = number  # Store the name-number pair

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names and numbers in the phonebook.
    """
    print("\nPhonebook Entries:")
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")


def lookup_numbers(phonebook):
    """
    Allow the user to look up phone numbers in the phonebook
    by searching for a name.
    """
    while True:
        name = input("\nEnter name to lookup (or press Enter to exit): ")
        if name == "":
            break  # Stop lookup when the user enters nothing
        if name not in phonebook:
            print(f"{name} is not in the phonebook.")
        else:
            print(f"{name}'s number: {phonebook[name]}")


def main():
    """
    Run the phonebook program by allowing users to add contacts,
    view the phonebook, and look up numbers.
    """
    phonebook = read_phone_numbers()  # Read phone numbers from user
    print_phonebook(phonebook)  # Display all contacts
    lookup_numbers(phonebook)  # Allow number lookups


# Python boilerplate.
if __name__ == '__main__':
    main()
