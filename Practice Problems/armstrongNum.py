num = input()
n = list(num)
l = len(n)
s = 0

for i in n:
    i = int(i)
    i = i**l
    s += i

if s == int(num):
    print("It's an Amstrong Number!")
else:
    print("It's not an Amstrong Number!")
