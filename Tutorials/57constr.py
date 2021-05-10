class Employee:
    def __init__(self, name, job, age):  
        self.name = name
        self.job = job
        self.age = age

    l = 43  # applied to whole class default but can be changed so that it is different for different obj
    
    def f1(self):
        return f'Name is {self.name}...Job is {self.job}...Age is {self.age}'

    @classmethod  # cls stands for class Name not for object
    def shortCut1(cls, string):
        x = string.split('-')
        return cls(x[0], x[1], x[2])   # now became a list
                #   OR
        # return cls(*string.split('/'))
                #   OR
        # name, job, age = string.split('/')
        # return cls(name, job, age)

    # --OR--
    @classmethod
    def shortCut2(cls, string):
        # x = string.split('/')
        # return cls(x[0], x[1], x[2])
        #   OR
        return cls(*string.split('/'))


ars = Employee('ARS', 'Coder', '19')
harry = Employee('Harry', 'Programmer', '28')
joe = Employee.shortCut1('Joe-CSS-30')
pip = Employee.shortCut2('Pip/JS/44')

print(joe.age)
print(joe.f1())
print(pip.f1())

print(Employee.l)
print(ars.l)