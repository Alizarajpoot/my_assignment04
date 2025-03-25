def main():
    numbers: list[int] = [1, 2, 3, 4]  # Create a list of numbers
    numbers = [num * 2 for num in numbers]  # Double each element using list comprehension
    print(numbers)  # Print the updated list

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
