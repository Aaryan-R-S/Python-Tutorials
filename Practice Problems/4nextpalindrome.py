inp = int(input("Enter the no of test cases :\n"))

i = 0
while i < inp:
    a = input(f"Enter the Number [{i+1}] : ")
    while True:
        if a == a[::-1]:
            print(a)
            break
        else:
            a = int(a)
            a += 1
            a = str(a)
    i += 1
