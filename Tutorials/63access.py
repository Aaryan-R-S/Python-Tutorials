'''
Public - Anyone can see
Private - You can see
Protected - Members can see 
'''

class Employee:

    no_of_leaves = 1      # PUBLIC VARIABLE -- Can be used anywhere
    _leaves = 2  # PROTECTED VARIABLE -- Can be used in this class and its sub-classes only
    __leaves = 3  # PRIVATE VARIABLE -- Can be accessed specially only

    def __init__(this, name, job, age):  
        this.name = name
        this.job = job
        this.age = age

    def infoEmployee(this):
        return f'Name is {this.name}...Job is {this.job}...Age is {this.age}'

    @classmethod
    def shortCut(this, string):
        x = string.split('-')
        return this(x[0], x[1], x[2])   # now became a list
  
    @staticmethod
    def static(x):
        print('Hi', x)
        return 'Lol'

jam = Employee.shortCut('Jam-40-Coder')
print(jam.__dict__)

print(Employee.no_of_leaves)
print(jam.no_of_leaves)

print(Employee._leaves)
print(jam._leaves)

print(jam._Employee__leaves)  # SECRET TO DECODE IT