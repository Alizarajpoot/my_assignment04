#Write a program to solve this age-related riddle!
#Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:Anton is 21 years old.
#Beth is 6 years older than Anton.
#Chen is 20 years older than Beth.
#Drew is as old as Chen's age plus Anton's age.
#Ethan is the same age as Chen.
#Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):
#Anton is 3
#Beth is 4
#Chen is 5
#Drew is 6
#Ethan is 7

def main():
    # Assign ages based on the given conditions
    anton = 21
    beth = anton + 6
    chen = beth + 20
    drew = chen + anton
    ethan = chen

    # Print out all of the ages
    print(f"Anton is {anton}")
    print(f"Beth is {beth}")
    print(f"Chen is {chen}")
    print(f"Drew is {drew}")
    print(f"Ethan is {ethan}")


# Required line to call the main function
if __name__ == '__main__':
    main()
