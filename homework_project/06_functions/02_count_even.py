def count_even(lst):
    """
    Returns number of even numbers in list.
    """
    count = sum(1 for num in lst if num % 2 == 0)  # More Pythonic way to count evens
    print(count)

def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []  # Empty list to store numbers
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":  # Stop when user presses enter
            break
        try:
            lst.append(int(user_input))  # Convert input to int and store
        except ValueError:
            print("Invalid input! Please enter an integer.")  # Handle invalid inputs gracefully
    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)

if __name__ == '__main__':
    main()
