a = int(input('Enter your first no : '))
b = int(input('Enter your second no : '))
c = input('Enter your operator\'s symbol [+,-,*,/] : ')

if a==45 and b==3 and c=='*':
    print('Answer : 555')
elif a==56 and b==9 and c=='+':
    print('Answer : 77')
elif a==56 and b==6 and c=='/':
    print('Answer : 4')
elif c=='*':
    print('Answer :', a*b)
elif c=='+':
    print('Answer :', a+b)
elif c=='/':
    print('Answer :', a/b)
elif c=='-':
    print('Answer :', a-b)
else:
    print('Check your inputs!')




