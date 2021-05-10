def getDateTime():
    import datetime
    return datetime.datetime.now()

def take (k):
    if k==1:
        c = int(input('Enter 1 for Exercise & 2 for Food : '))
        if c==1:
            data = input("Type Here:\n")
            with open('Tuts/37/Tom-exercise.txt', 'a') as e:
                e.write(str([str(getDateTime())])+ ': '+ data + '\n')
                print('Successfully Added!')
        elif c==2:
            data = input("Type Here:\n")
            with open('Tuts/37/Tom-food.txt', 'a') as e:
                e.write(str([str(getDateTime())])+ ': '+ data + '\n')
                print('Successfully Added!')

    elif k==2:
        c = int(input('Enter 1 for Exercise & 2 for Food : '))
        if c==1:
            data = input("Type Here:\n")
            with open('Tuts/37/Pop-exercise.txt', 'a') as e:
                e.write(str([str(getDateTime())])+ ': '+ data + '\n')
                print('Successfully Added!')
        elif c==2:
            data = input("Type Here:\n")
            with open('Tuts/37/Pop-food.txt', 'a') as e:
                e.write(str([str(getDateTime())])+ ': '+ data + '\n')
                print('Successfully Added!')

    elif k==3:
        c = int(input('Enter 1 for Exercise & 2 for Food : '))
        if c==1:
            data = input("Type Here:\n")
            with open('Tuts/37/Kip-exercise.txt', 'a') as e:
                e.write(str([str(getDateTime())])+ ': '+ data + '\n')
                print('Successfully Added!')
        elif c==2:
            data = input("Type Here:\n")
            with open('Tuts/37/Kip-food.txt', 'a') as e:
                e.write(str([str(getDateTime())])+ ': '+ data + '\n')
                print('Successfully Added!')

def retrieve(k):

    if k==1:
        c = int(input('Enter 1 for Exercise & 2 for Food : '))
        if c==1:
            with open('Tuts/37/Tom-exercise.txt') as e:
                for char in e :
                    print(char, end="")
                # OR
                # print(e.read())
        elif c==2:
            with open('Tuts/37/Tom-food.txt') as e:
                for char in e :
                    print(char, end="")

    elif k==2:
        c = int(input('Enter 1 for Exercise & 2 for Food : '))
        if c==1:
            with open('Tuts/37/Pop-exercise.txt') as e:
                for char in e :
                    print(char, end="")
        elif c==2:
            with open('Tuts/37/Pop-food.txt') as e:
                for char in e :
                    print(char, end="")

    elif k==3:
        c = int(input('Enter 1 for Exercise & 2 for Food : '))
        if c==1:
            with open('Tuts/37/Kip-exercise.txt') as e:
                for char in e :
                    print(char, end="")
        elif c==2:
            with open('Tuts/37/Kip-food.txt') as e:
                for char in e :
                    print(char, end="")


print(' ')
print('Welcome to Health Management System!')
a = int(input('Enter 1 to View & 2 to Add : '))

if a==2 :
    b = int(input("Enter 1 for Tom, 2 for Pop & 3 for Kip : "))
    take(b)
elif a==1:
    b = int(input("Enter 1 for Tom, 2 for Pop & 3 for Kip : "))
    retrieve(b)
