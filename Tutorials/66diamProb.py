class A:
    def f1(this):
        print('This is A')

class B(A):
    def f1(this):
        print('This is B')

class C(A):
    def f1(this):
        print('This is C')
    pass

class D(B, C):
    #  Class Function --
    def f1():
        print('This is D')

    #  Object Function --
    def f1(this):
        print('This is D')


a = A()
b = B()
c = C()
d = D()

d.f1()