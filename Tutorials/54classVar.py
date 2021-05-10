class Employee:
    language = 'python'
    pass

ars = Employee()
harry = Employee()

ars.name = 'ARS'
ars.job = 'Coder'
ars.age = 19
ars.language = 'Node'
print(ars.__dict__)

harry.name = 'Harry'
harry.job = 'Programmer'
harry.age = 28
harry.language = 'JS'
print(harry.__dict__)   # see language is printed specially for Harry only as it sis changed

print(Employee.language)
print(ars.language)
print(harry.language)
print(Employee.__dict__)