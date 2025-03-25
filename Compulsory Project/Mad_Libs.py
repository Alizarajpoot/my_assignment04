
#project1

def mad_libs():
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")

    story = f"One day, a {adjective} {noun} decided to {verb} at the {place}. It was an unforgettable adventure!"

    print("\nYour Mad Libs story:\n")
    print(story)

mad_libs()
