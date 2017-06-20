# Name:Kyle Bomar
# Date:6/20/17

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""

"""
x = int(raw_input('How many Fibonacci numbers would you like to generate?'))

a=0
b=1
for numbers in range (1,x+1):
    if numbers== 1:
        FN =a+b
        print FN
    else:
        FN = a+b
        print FN

        a=b
        b=FN
"""


x= int(raw_input("How many Fibonacci numbers would you like to generate?"))
number = 1
b = 0
a= 1
while number < (x+1):
