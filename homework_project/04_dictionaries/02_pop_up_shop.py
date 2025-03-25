def main():
    # Dictionary of available fruits and their prices
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }
    
    total_cost = 0  # Initialize total cost

    # Loop through the fruits dictionary
    for fruit_name, price in fruits.items():
        # Ask user how many of each fruit they want
        amount_bought = int(input(f"How many ({fruit_name}) do you want to buy?: "))
        total_cost += price * amount_bought  # Add to total cost

    # Print total cost
    print(f"Your total is ${total_cost:.2f}")  # Format to 2 decimal places


# Required line to execute the main function
if __name__ == '__main__':
    main()
