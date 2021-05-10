# Lambda(Anonymous) Functions--

def add(a, b):
    return a+b
print(add(6,8))

# BOTH SAME 

add = lambda a,b : a+b
print(add(6,8))

# SORTING WITH LAMBDA
p = [[21,3], [2,27], [4,2]] 

p.sort(key = lambda x : x[0])      # key takes a function
print(p)                         # sort on basis of 1st elem

p.sort(key = lambda x : x[1])      # key takes a function
print(p)                         # sort on basis of 2nd elem

j = [1,32,4,6,0,67]
j.sort()
print(j)