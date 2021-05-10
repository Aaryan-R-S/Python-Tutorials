print(" ")
print('Welcome to Pattern Generator!')

try:
    patternStyle = None
    num = int(input('Enter a Number between 1 to 9 for length of Pattern : '))
    style = input('Enter + or - to get Pattern in ascending or descending form : ')

    if style == '-':
        patternStyle = False
    elif style == '+':
        patternStyle = True

    if patternStyle==True:
        i = 0
        while i<num:
            print(('*'*(2*i+1)).center(18))
            # print(('*'*(2*i+1)).rjust(18))
            # print(('*'*(2*i+1)).ljust(18))
            i+=1

    elif patternStyle==False:
        i = num-1
        while i>=0:
            print(('*'*(2*i+1)).center(18))
            i-=1
except :
    print('Invalid Inputs!')

print(" ")
