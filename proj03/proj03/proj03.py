# Name:Kyle Bomar
# Date:6/20/17


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
import random

variable_name = random.randint(1,9)



x = int(raw_input("Please guess a number betwwen 1 and 9:"))
#print "Your answer:", x

#print "Correct answer:", variable_name

if x < variable_name:
    print "Sorry, you guessed too low."

if x > variable_name:
    print "Sorry, you guessed too high."

if x == variable_name:
    print "Congratulations, you guessed the correct number "

while x != variable_name:
    x=int(raw_input('Guess again?'))








#x = int(raw_input("Please guess a number betwwen 1 and 9:"))
#print "Your answer:", x






    if  x < variable_name:
        #print "Your answer:", x
        print "Sorry, you guessed too low."



    if x> variable_name:
        #print "Your answer:",x
        print "Sorry, you guessed too high."



    if x==variable_name:
        #print "Your answer:", x
        print "Congratulations, you guessed the correct number "





k=raw_input("Type exit to end program.")