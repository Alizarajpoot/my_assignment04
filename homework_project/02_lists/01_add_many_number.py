def add_many_numbers(numbers: list[int]) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    return sum(numbers)  # More concise and efficient

# Main function to test
def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  # Example list of numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # Find the sum
    print(sum_of_numbers)  # Print the result

if __name__ == '__main__':
    main()
