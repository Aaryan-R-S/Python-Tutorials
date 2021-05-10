n = 10   # global scope

def func1():
    # n+=1   not POSSIBLE
    n=5  # local scope
    print(n) 

print(n)   #10
func1()    #5


i = 0
def f1():
    i=1
    print(i)
    def f2():
        global i
        i=2
    f2()


print(i)  # bcz of top i=0 existed first
f1()      # bcz i=1 has local scope
print(i)  # bcz f2 changed global i to 2