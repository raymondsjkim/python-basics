'''
Raymond Kim
01/11/2018
Python Assignment 1
'''

#Get user input
number = input("Enter an integer between 6 and 24: ")
#Convert str to int
number = int(number)

if number < 6 or number > 24:
    print("This is the case");
elif 6 < number <= 12:
    print("Congratulations")
else:
    number = number - 6
    print("Your number has been changed to:", number)
