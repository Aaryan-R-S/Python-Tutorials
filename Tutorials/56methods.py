class Employee:
    # k is class var but thus.k is instance var at object level 
    k = 2
    def __init__(this, name, job, age):  
        this.name = name
        this.job = job
        this.age = age
        this.k = 20

    def f1(this):
        return f'Name is {this.name}...Job is {this.job}...Age is {this.age}'

    # THIS WILL APPLY TO PARTICULAR OBJECT--
    def enterLeaves(this, leaves):
        this.leaves = leaves

    # THIS WILL APPLY TO WHOLE CLASS EVEN IF YOU APLIED TO ONE OBJECT TOO--
    # @classmethod
    # def enterLeaves(this, leaves):
    #     this.leaves = leaves


ars = Employee('ARS', 'Coder', '19')
harry = Employee('Harry', 'Programmer', '28')

ars.enterLeaves(2)
harry.enterLeaves(4)

print(ars.leaves)
print(harry.leaves)

print(ars.f1())
print(harry.f1())

ars.k = 4 # instance var 

print(ars.k, harry.k, Employee.k)

Employee.k = 3 # Employee.k is class var

lol = Employee("Lol","wer","34")
print(lol.k, Employee.k)

