print("")
num1 = int(input("Enter your First Num : "))
num2 = int(input("Enter your Second Num : "))

def lcm(num1, num2):
    maxnum = max(num1,num2)

    if maxnum == num1:
        while maxnum%num2 != 0:
            maxnum += num1
    else:
        while maxnum%num1 != 0:
            maxnum += num2
            
    return maxnum

print("")
print(f"L.C.M of {num1} and {num2} is {lcm(num1,num2)}")
print("")
