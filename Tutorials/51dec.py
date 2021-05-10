#   ----- 1 -----

# def f1():
#     print('Hi')

# f2 = f1

# f2()


#   ----- 2 -----

# def f1():
#     print('Hi')

# f2 = f1

# del f1

# f2()

#   ----- 3 -----

# def f1(x):
#     x('Yo')

# f1(print)

# -- Or --

# def f2(x):
#     print(x([3,4,5]))

# f2(sum)


#   ----- 4 -----

# def f1(x):
#     def f2():
#         print('Executing')
#         x()
#         print('Executed')
#     return f2

# def f3():
#     print('Hello')

# f3 = f1(f3)
# f3()

