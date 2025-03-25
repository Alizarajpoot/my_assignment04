from hashlib import sha256

def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.

    email: the email we are checking the password for
    stored_logins: a dictionary pointing from an email to its hashed password
    password_to_check: a password we want to test alongside the email to login with
    """
    # Check if the email exists in the stored logins
    if email in stored_logins and stored_logins[email] == hash_password(password_to_check):
        return True
    
    return False

# Function to hash a password
def hash_password(password):
    """
    Takes in a password and returns the SHA256 hashed value for that specific password.
    
    Inputs:
        password: the password we want
    
    Outputs:
        the hashed form of the input password
    """
    return sha256(password.encode()).hexdigest()

def main():
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        "example@gmail.com": hash_password("password"),
        "code_in_placer@cip.org": hash_password("Karel"),
        "student@stanford.edu": hash_password("123!456?789")
    }
    
    # Test cases
    print(login("example@gmail.com", stored_logins, "word"))        # False
    print(login("example@gmail.com", stored_logins, "password"))    # True
    
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))  # True
    print(login("code_in_placer@cip.org", stored_logins, "karel"))  # False
    
    print(login("student@stanford.edu", stored_logins, "password")) # False
    print(login("student@stanford.edu", stored_logins, "123!456?789")) # True


if __name__ == '__main__':
    main()
