# l = []

# for i in range(100):
#     if i%3 == 0:
#         l.append(i)

# print(l)

#  OR

# List --
# l = [i for i in range(100) if i%3==0]
# print(l)

#  OR

# Dictionary --
# d = {i: f"Item {i}" for i in range(1000) if i%100==0}
# print(d)

#  OR

# Dictionary --
# d = {i: f"Item {i}" for i in range(5)}
# print(d)
# d = {value:key for key,value in d.items()}
# print(d)


#  OR

# Set--

# s = set({i for i in range(5,10)})
# print(s)


#  OR
# Generator -- 

# q = (i for i in range(10) if i%2 == 0)

# for Q in q:
#     print(Q)

# Or using q.__next__()

# l = {'a':45, 'A':30, 'b':24, 'B':1}
# j = {k.lower(): l[k.lower()]+l[k.upper()] for k in l.keys()}
# print(j)

# print({'a':1, 'a':1})