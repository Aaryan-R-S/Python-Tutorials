'''
Iterable - methods : __iter__() or __getitem__()       means capable of iteration
  e.g. strings, range but not int
Iterator - __next__()  [GENERATORS]
Iteration - process of iterating
'''

#   -- 1 --
# Generator --       [generate nos on the spot] 
# for i in range(10000):
#     print(i)


#   -- 2 --
# Custom Generator --  [generate only when called]
def generator1(n):
    for i in range(n):
      yield i

x = generator1(5)
print(x)

# print(next(x)) 
# print(next(x)) 
# print(next(x)) 
# print(next(x)) 
#  # -- OR --
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
# print(x.__next__())   # give error



#   -- 3 --
# y = iter(43453)  not possible
y = iter('Qwerty')
# print(y)

for i in y:
  print(i) 

# -- OR --

# print(y.__next__())
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())     # give error



#   -- 4 --
def genFibNo(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a,b  =   b,a + b

f = genFibNo(11)
print(f)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
# print(f.__next__())

