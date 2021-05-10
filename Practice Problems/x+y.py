def move(mylist):
    for i in range(len(mylist)-1):
        if mylist[i] == '1':
            mylist[i] = '0'
            if mylist[i+1] == '0':
                mylist[i+1] = '1'
            else:
                mylist[i+1] == '0'
    return mylist

if __name__ == "__main__":
    a = list('1011111111111')
    print(a)
    while a != move(a.copy()):
        a = move(a.copy())

    print(a)