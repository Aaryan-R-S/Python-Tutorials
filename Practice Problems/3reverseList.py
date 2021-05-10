print("Press Enter to enter an Item & Double Enter to when Done !")
myList = []

while True:
    inp = input()
    if inp == "":
        break
    else:
        myList.append(inp)

print(myList)

# -- 1 --
print(myList[::-1])

# -- 2 --
myList2 = myList[:]  # make an copy
myList2.reverse()
print(myList2)

# -- 3 --
myList3 = myList[:]
l = len(myList3)
if l%2==0:
    i=0
    while i<(l/2):
        myList3[i], myList3[l-i-1] = myList3[l-i-1], myList3[i]
        i+=1

else:
    i=0
    while i<((l+1)/2 - 1):
        myList3[i], myList3[l-i-1] = myList3[l-i-1], myList3[i]
        i+=1

print(myList3)
print(myList)

