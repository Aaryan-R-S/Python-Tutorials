#  -- 1 --

class A:
    x = "I'm in Class A."           # Class variable

    def __init__(this):
        this.x = "Instance var in class A"            # Instance variable

class B(A):
    x = "I'm in class B."            # Class variable


a = A() 
b = B() 

print(b.x)

#  First searches Instance Variables in B then in A
#  Then searches Class Variables in B then in A




#  -- 2 --

class A:
    x = "I'm in Class A."           # Class variable

    def __init__(this):
        this.x = "Instance var in class A"            # Instance variable

class B(A):
    x = "I'm in class B."            # Class variable

    def __init__(this):
        this.x = "Instance var in class B"            # Instance variable


a = A() 
b = B() 

print(b.x)
#  now b is printed as method is overwritten





#  -- 3 --

class A:
    x = "I'm in Class A."           # Class variable

    def __init__(this):
        this.x = "Instance var in class A"            # Instance variable
        this.j = 2

class B(A):
    x = "I'm in class B."            # Class variable

    def __init__(this):
        this.x = "Instance var in class B"            # Instance variable
        super().__init__()  # Way to call super class same method which is over written
        # this.x = "Instance var in class B"            # Instance variable


a = A() 
b = B() 

print(b.j)  #this can be called bcz of super().__init__()
print(b.x)

#  A is printed bcz we have again over written B __init__method



