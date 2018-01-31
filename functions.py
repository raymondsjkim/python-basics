
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
