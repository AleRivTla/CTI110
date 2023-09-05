"""
CTI 110
P1H1 - Variables
Rivera Alejandro
9/5/2023

Do some basic output with numbers
1. ask for an int
2. square it and then cube it
3. ask for another int
4. add them and multiply them

"""
# PART 1: Numbers
# variables, first and second
first = 0
second = 0

print("Enter integer:")
first = int(input()) # take input, then convert it to an int
print(first, "squared is", first * first)
print("and", first, "cubed is", first * first * first, "!!")

# get another int
print("Enter another integer:")
second = int(input())
# TODO: print the number, not the words first and second
# print("first + second =", first + second)
print(first, "+", second, "=", first + second)
#print("first * second =", first * second)
print(first, "*", second, "=", first * second)

# PART 2: Movies
# Three variables
# string - movie name
# int - the year of the movie
# float - the gross (in million dollars)

name = "Oppenheimer"
year = 2023
gross = 853.24 # mil $

# Print out this information
# Then print a movie quote

# adding space between parts.
print("""


""")
# spacing ends
print("The movie", name, "came out in", year, "and made a total of $",  gross, "million.")
print("My favorite quote from the movie is: I have become Death, destroyer of worlds.")


