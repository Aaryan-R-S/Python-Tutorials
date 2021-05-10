num = int(input('Enter the number : '))

# ITERATIVE APPROACH :
def factorialIterative(n):
    fac = 1
    i = 0
    for i in range(n) :
        fac = fac*(i+1) 
    return fac

for i in range(num) :
    print('Factorial of',i+1 ,':',factorialIterative(i+1))


# RECURSIVE APPROOACH :
def factorialRecursive(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorialRecursive(n-1)


print('Using Recursive Method : Factorial')
print(factorialRecursive(num))


# Fibonacci Sequence --

def fibonacciNums(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacciNums(n-1)+fibonacciNums(n-2)
print('Fibonacci n(th) number :',fibonacciNums(num))


def fibonacciNums(n):
    a, b = 0, 1
    for i in range(n):
        a,b  =   b,a + b
    return a

for i in range(num) :
    print('Fibonacci',i+1 ,'(th) number :',fibonacciNums(i))


