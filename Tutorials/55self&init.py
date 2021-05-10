class Employee:
    increament = 1.5
    employeePopulation = 0
    # CONSTRUCTOR :
    def __init__(self, name, job, age):  # self is necessary !
        self.name = name
        self.job = job
        self.age = age
        self.increament = 2
        Employee.employeePopulation +=1  # count no. of objects
    
    def increase(self):
        # self.age = self.age * increament   # WRONG
        self.age = self.age * self.increament  # [2] RIGHT IF TAKING INSTANCE VARIABLE & then go for class variable
        self.age = self.age * Employee.increament  # [1.5] RIGHT IF TAKING CLASS VARIABLE only

    # Applies to all!
    leaves = 8
    
    # METHODS -- (x is used as self)
    def f1(self):
        return f'Name is {self.name}...Job is {self.job}...Age is {self.age}'

ars = Employee('ARS', 'Coder', 19)
harry = Employee('Harry', 'Programmer', 28)

# ars.name = 'ARS'
# ars.job = 'Coder'
# ars.age = 19
ars.leaves = 2

# harry.name = 'Harry'
# harry.job = 'Programmer'
# harry.age = 28
# harry.language = 'JS'

print(ars.leaves)
print(ars.f1())
print(harry.f1())

# IMPortant --
print(harry.age)
harry.increase()
print(harry.age)


print(harry.__dict__)
print(Employee.__dict__)

print(Employee.employeePopulation)

