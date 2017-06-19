# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

name = raw_input("Enter your name: ")
age = int(raw_input("Enter your age: "))
birthday = raw_input("Has your birthday happened this year? Enter Y or N: ")

if birthday == "Y":
    # Calculates the year that the user will be 100
    year = 2017

else:
    year = 2016
    # Calculates the year that the user will be 100
for variable in range(age,100):
    year = year +1

print name, " will turn 100 in the year ", year, "."

