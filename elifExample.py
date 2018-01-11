#elifExample.py

#Get integer:
number=input("Enter a positive integer: ")

#Convert the integer from string to integer:
number=int(number)

if number <= 0:
    print(number, "<", 5)
    print("That's a good thing!")
    print("I'm done now.")
elif 5 <= number < 10:
    print(5, "<=", number, "<10")
else:
    print(number, "is too big. I had to take a nap.")
