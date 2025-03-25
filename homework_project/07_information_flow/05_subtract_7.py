def subtract_seven(num: int) -> int:
    """Subtracts 7 from the given number and returns the result."""
    return num - 7  # Simplified operation

def main():
    num = 7  # Initial number
    num = subtract_seven(num)  # Call the function and update num
    print("This should be zero:", num)  # Output result

if __name__ == '__main__':
    main()
