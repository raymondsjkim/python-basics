#1
'''
Raymond Kim
01/18/2018
Looping Quantifiers (Part A)
'''

#2
'''
Prints the square of every other integer between
-5 through 20, starting with -5.
'''
for x in range(-5,21,2):
    print("The square of",x,"is:",x**2)

#3
'''
Add in strings to phrase from list L
and print
'''   
L=["mayhem","chaos","robert","paulson","durden"]
phrase=""
for word in L:
    phrase = phrase + word.upper() + ", "
    
print(phrase)


#4
'''
Raymond Kim
01/18/2018
Looping Quantifiers (Part B)
'''

#5
S=set(range(2,102,2))
truth_value_s=False
for x in S:
    if 2 < (x**3 - 2*x**2) <= 50:
        truth_value_s=True
        break
    
print(truth_value_s)

#6
phrase="This sentence referencing itself"
truth_value_x=True

for x in phrase.lower():
    if "t" not in x:
        truth_value_x=False
        break
    
print(truth_value_x)

#7
'''
#5 rewritten
'''
anyS=any(2 < (x**3 - 2*x**2) <= 50 for x in range(2,102,2))
print(anyS)
'''
#6 rewritten
'''
allX=all("t" not in x for x in phrase.lower())
print(allX)
