def double(num: int) -> int:
    """
    Returns the result of multiplying num by 2.
    """
    return num * 2

def main():
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")

    num_times_2 = double(num)
    print("Double that is", num_times_2)

if __name__ == '__main__':
    main()
