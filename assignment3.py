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


'''
Function and Sets II
Raymond Kim
01/30/2018
'''

def sumUp(*X):
    s=0
    for x in X:
        s=s+x
    return s

print(sumUp(10,50,1000))

def f(x):
    return x**2 - 2*x + 7

def g(k):
    return (k+1)**2 / (3*k+2)

A=set(range(1,21))
im_f = {f(a) for a in A}
print(im_f)


A={2,4,6,8,10}
im_g = {g(a) for a in A}
print(A)
print(im_g)


def f(x):
    return 2*x - 1

A=set(range(1,11))
B=set(range(1,20,2))
im_f = {f(a) for a in A}
print(any(x for x in B-im_f))


def h(x):
    return x**3 + 5
print(all(h(x) for x in range(-100,101) if x != 0))
