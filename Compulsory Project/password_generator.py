#project 7

import random
import string

def generate_password(length=12):
    """Generate a random password with uppercase, lowercase, digits, and special characters."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password length
while True:
    try:
        length = int(input("Enter the desired password length: "))
        break  # Exit loop if input is a valid integer
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

password = generate_password(length)
print("🔐 Your generated password:", password)