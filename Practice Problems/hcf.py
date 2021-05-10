print("")
num1 = int(input("Enter your First Num : "))
num2 = int(input("Enter your Second Num : "))

def hcf(num1, num2):
    minnum = min(num1,num2)

    if minnum == num1:
        while num2%minnum != 0 or num1%minnum != 0 :
            minnum -= 1
    else:
        while num1%minnum != 0 or num2%minnum !=0 :
            minnum -= 1
            
    return minnum

print("")
print(f"H.C.F of {num1} and {num2} is {hcf(num1,num2)}")
print("")
