with open('currency.txt') as f:
    a = f.readlines()

listCurr = []
for line in a:
    part = line.split("\t")
    listCurr.append(part[0])

print(" ")
print("Welcome to Currency Convertor!")
print(" ")
i=0
while i in range(len(listCurr)):
    if i != len(listCurr)-1:
        print(listCurr[i], end=", ")
    else:
        print(listCurr[i])
    i+=1

def finder(currencyFrom, currencyTo, amt):
    c1 = None
    c2 = None
    part = None
    parted = None

    for line in a:
        part = line.split("\t")
        if part[0] == currencyFrom:
            parted = part[2].split("\n") 
            c1 = float(parted[0])
        elif part[0] == currencyTo:
            parted = part[2].split("\n") 
            c2 = float(parted[0])

    return c1/c2 * amt

currencyFrom = input("\nFrom : ")
currencyTo = input("\nTo : ")
amt = float(input("\nAmount : "))

print(finder(currencyFrom, currencyTo, amt))