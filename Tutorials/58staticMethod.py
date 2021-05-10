class Employee:
    def __init__(this, name, job, age):  
        this.name = name
        this.job = job
        this.age = age

    def f1(this):
        return f'Name is {this.name}...Job is {this.job}...Age is {this.age}'
    
    @staticmethod
    def f2(x):
        print('Hi', x)
        return 'Lol'

ars = Employee('ARS', 'Coder', '19')

print(ars.f2(ars.name))   # call func + print return value
ars.f2(ars.name)    # call func
#  OR
Employee.f2(ars.name)

# IMPORTANT --
# can't be called like f2()
# should be called as [nameOfAnyObjectORnameOfClass].f2()
