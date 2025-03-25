MAX_LENGTH: int = 3  # Maximum allowed length of the list

def shorten(lst):
    """
    Removes elements from the end of lst until its length is MAX_LENGTH.
    Prints each removed item.
    """
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()  # Remove the last element
        print(last_elem)  # Print the removed element

def get_lst():
    """
    Prompts the user to enter elements one by one and returns the final list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":  # Continue until the user presses Enter
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()  # Get user input as a list
    shorten(lst)  # Shorten the list if needed

if __name__ == '__main__':
    main()
