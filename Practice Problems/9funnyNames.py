import random

num = int(input("Enter the no of names : "))
names = []
fun1 = []
fun2 = []
fun3 = []

for i in range(num):
    name = input(f"Enter Name {i+1} : ")
    names.append(name)    

for nm in names:
    n = nm.split(" ")
    fun1.append(n[0])
    fun2.append(n[1])
    for i in range(len(n)-2):
        fun3.append(n[i+2])

fun = []

for i in range(num):
    if fun3 == []:
        r1 = random.choice(fun1)
        r2 = random.choice(fun2)
        fun.append(r1 +" "+ r2)
        fun1.remove(r1)
        fun2.remove(r2)
    else:
        r1 = random.choice(fun1)
        r2 = random.choice(fun2)
        r3 = random.choice(fun3)
        fun.append(r1+" "+ r2+" "+r3)
        fun1.remove(r1)
        fun2.remove(r2)
        fun3.remove(r3)


print(fun)


