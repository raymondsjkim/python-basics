'''
Raymond Kim
01/18/2018
Looping Quantifiers (part A)
'''

'''
Prints the square of every other integer between
-5 through 20, starting with -5.
'''
for x in range(-5,21,2):
    print("The square of",x,"is:",x**2)


'''
Add in strings to phrase from list L
and print
'''   
L=["mayhem","chaos","robert","paulson","durden"]
phrase=""
for word in L:
    phrase = phrase + word.upper() + ", "
print(phrase)
