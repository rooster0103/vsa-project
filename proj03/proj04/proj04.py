# Name:Kyle Bomar
# Date: 6/20/17

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""

x = raw_input('Please insert a string:')
alist=[]
reverse_list=[]
for letter in x:
    alist.append(letter)

y=len(alist)
hat=x
for letter in range(1,y+1):
    reverse_list.append(x[-1])
    x=x[:-1]




if hat == reverse