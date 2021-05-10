class Employee:

    #  Dunder Method (__func__)
    def __init__(this, name, job, age):  
        this.name = name
        this.job = job
        this.age = age

    #  SPECIAL Dunder Method (__func__)
            # SEARCH ON WEB  : MAPPING OPERATORS TO FUNCTIONS

    def __str__(this):
        return f'Employee({this.name} | {this.job} | {this.age})'
    def __repr__(this):
        return f'Employee(Name : {this.name} | Job : {this.job} | Age: {this.age})'
    
    # Use str or repr [both same] in presence of both str will be given preferenece --

    def __add__(this, that):        # TURN + TO ADD AGE FUNC
        return this.age + that.age

    def __truediv__(this, that):        # TURN / TO AGE DIVIDE FUNC
        return this.age / that.age

    def __mul__(this, that):        # TURN * TO MULTIPLY AGE FUNC
        return this.age * that.age


    def f1():   # applies to class only (without arguments)
        return 'Hi'

    def f2(this):  # applies to both class & objects but specially for objects (with atleast one argument)
        return 'Hi'

    @classmethod  # applies to class only (with arguments)
    def shortCut(this, string):
        x = string.split('-')
        return this(x[0], x[1], x[2])   # now became a list
  
    @staticmethod  # applies to both class & object but is not meant to modify them or related to them
    def f2(x):
        print('Hi', x)
        return 'Lol'

joe = Employee('Joe', 'Coder', 34)
poe = Employee('Poe', 'Coder', 44)

print(joe)  # default str
print(repr(joe))
#  in absence of __repr__ it will give object id

print(joe+poe) 
#  OR
print(joe.__add__(poe)) 
#  in absence of __add__ it will give error

print(joe*poe) 
print(joe/poe) 
