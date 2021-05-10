# -- Maps --

# nums = ['1', '2', '3']

# for i in range(len(nums)):
#     nums[i] = int(nums[i])

#   -- OR --

# nums = list(map(functionName, listName))
# nums = list(map(int, nums))

# nums[2] += 1
# print(nums[2])


# Map Special --

# nums = list(map(int, nums))
# squareList = list(map(lambda x: x*x, nums))
# print(squareList)

# cubeList = list(map(lambda x: x*x*x, nums))
# print(cubeList)


# PRINT NUM + SQUARE + CUBE --

# def num(a):
#     return a

# def square(a):
#     return a*a

# def cube(a):
#     return a*a*a

# sqCu = [num, square, cube]
# for i in range(10):
#     val = list(map(lambda x:x(i), sqCu))
#     print(val)



# Filter --

# p = [1,2,3,4,5,6,7,8,9]

# def greatThan5(n):
#     return n>5

# o = list(filter(greatThan5, p))
# print(o)


#  Reduce --

# from functools import reduce

# p = [1,2,3,4]
# o = reduce(lambda x,y : x+y, p)
# print(o)

# -- OR --

# print(sum(p))