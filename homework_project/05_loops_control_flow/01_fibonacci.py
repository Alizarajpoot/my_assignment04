MAX_TERM_VALUE = 10000  # Maximum value for Fibonacci sequence

def main():
    curr_term = 0  # Fib(0)
    next_term = 1  # Fib(1)
    
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")  # Print Fibonacci term on the same line
        term_after_next = curr_term + next_term  # Calculate the next term
        curr_term = next_term  # Move to the next term
        next_term = term_after_next  # Update for the next iteration

    print()  # Print a newline after the sequence ends

if __name__ == '__main__':
    main()
