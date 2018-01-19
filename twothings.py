'''
Prints the cube of each x in the range 1 to 25
Fill in listified with the cubed values
'''
listified=[]
for x in range(1,26):
    print("The cube of",x,"is:",x**3)
    listified = listified + [x**3]

print(listified);
