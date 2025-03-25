def main():
    for i in range(10, 20):  # Loop from 10 to 19
        if is_odd(i):
            print(f"{i} odd")
        else:
            print(f"{i} even")

def is_odd(value: int) -> bool:
    """
    Checks if a value is odd. Returns True if it is, otherwise False.
    """
    return value % 2 == 1  # Returns True if remainder is 1 (odd number)

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
