num = False
maxNum = False
minNum = False

while True:
    try:
        num = int(input("Num : "))
        minNum = int(input("Min Num : "))
        maxNum = int(input("Max Num : "))
    except Exception as e:
        print("[ERROR] Please Enter a Whole Number", e)
    else:
        if num>=1 and maxNum>=2 and minNum>=1:
            if minNum<=maxNum:
                break
            else:
                print("[Error] Min is greater than Max!")
        else:
            print("[ERROR] Please Enter a Whole Number (Num>=1 and MinNum>=1 and MaxNum>=2)")

l = maxNum-minNum
i=-1
while i<l:
    if num%(minNum+i+1) == 0:
        print(f"{minNum+i+1} is a divisor of {num}")
    else:
        print(f"{minNum+i+1} is not a divisor of {num}")
    i+=1
