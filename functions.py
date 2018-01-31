
#Functions
def square(x):
    return x**2

print("The square of 2 is", square(2))

def sayHi():
    print("Hi")
    
sayHi()

def linear(a,b,x):
    print(a*x+b)
    return x*x+b

linear(2,3,-1.5)
linear(1.5,6,2/3)

def doubleIt(s):
    return 2*s

print(doubleIt(3))
print(doubleIt("cat"))


#Keyword Arguments
def sayHi(name="Jeff",age=24):
    print("Hi",name)
    print("You are",age,"years old.")

sayHi()
sayHi(age=36)
sayHi(age=15,name="Chadworth")

def goodVibes(x,name="Dr C"):
    print(name,"is sending you",x,"many good vibes.")

goodVibes(3)
goodVibes(75,name="Timmy")


#Variadic Functions
def mySum(*X):
    s=0
    for x in X:
        s+=x
    return s

print(mySum(*[1,2]), mySum(1,2,3), mySum(1,2,3,4,5))

print(mySum(*range(1001)))

#Functions in Functions

def f(k):
    return k**2 + 2*k + 1

def g(k):
    return k**3 - k

def sumUp(start,end,F):
    return sum([F(k) for k in range(start,end+1)])

print(sumUp(0,10,f))
print(sumUp(0,10,g))


'''
The code above generates the results for the summations:

 _10_
 \    k^2 + 2k + 1
 /___
 k = 0

 AND

  _10_
 \    k^3 - k
 /___
 k = 0
 
'''

#Advanced Feature
def sumUp(start,end,F):
    return sum([F(k) for k in range(start,end+1)])

print(sumUp(0,10,lambda k: k**4-2*k**3 + 5))
