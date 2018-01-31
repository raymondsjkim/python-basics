'''
Python Set Practice
Raymond Kim
01/30/2018
'''

Odds = set(range(1,200,2))
print(Odds)

Squares={x**2 for x in range(1,15)}
print(Squares)

StakeOutO = Squares-Odds
print("The set Squares-Odds is:", StakeOutO)

PerfSq={x**2 for x in range(1,32)}
print(len(PerfSq))

PerfCube={x**3 for x in range(1,11)}
print(len(PerfCube))
