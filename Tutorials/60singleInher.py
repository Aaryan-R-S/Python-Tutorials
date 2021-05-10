class Employee:
    def __init__(this, name, job, age):  
        this.name = name
        this.job = job
        this.age = age

    def f1(this):
        return f'Name is {this.name}...Job is {this.job}...Age is {this.age}'

    @classmethod
    def shortCut(this, string):
        x = string.split('-')
        return this(x[0], x[1], x[2])   # now became a list
  
    @staticmethod
    def f2(x):
        print('Hi', x)
        return 'Lol'

ars = Employee('ARS', 'Coder', '19')
harry = Employee('Harry', 'Developer', '28')


# Single Inheritance --
class Programmer(Employee):
    def __init__(this, name, job, age, experience):
        super().__init__(name, job, age)
        this.experience = experience


pip = Programmer('Pip', 'Programmer', '25', '20+yrs')

print(pip.__dict__)
print(pip.f1())
# help(Programmer)