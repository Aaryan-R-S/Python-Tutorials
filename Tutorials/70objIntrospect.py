class A:
    def __init__(this, fname, lname):
        this.fname = fname
        this.lname = lname

    def info(this):
        return f"The Employee is {this.fname} {this.lname}"

    @property
    def email(this):
        if this.fname == None or this.lname == None :
            return 'Email is not set. Please set it using setter!'
        return f'{this.fname}.{this.lname}@gmail.com'

    @email.setter  
    def email(this, string):
        print('Setting Now...')
        names = string.split('@')[0]
        this.fname = names.split('.')[0]
        this.lname = names.split('.')[1]

    @email.deleter
    def email(this):
        print('Deleting Now...')
        this.fname = None
        this.lname = None

x = A('Nik', 'Pik')

#  Object Introspection means details of object :

# TYPE -- (data type)
print(type('x'))  # class = str
print(type(x))  # class = A
print(" ")

# ID -- (unique changes everytime)
print(id('x'))
print(id(x))
print(" ")

# DIR -- (func)
print(dir('x'))
print(dir(x))
print(" ")

import inspect
print(inspect.getmembers(x))
print(x.__dict__)