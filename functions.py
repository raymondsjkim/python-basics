
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
