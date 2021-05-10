string = input()

if string == string[::-1]:
    print("Yes! It's a Palindrome... ",end=": ")
    print(string[::-1])
else:
    print("It's not a Palindrome... ",end=": ")
    print(string[::-1])
    
# make string shift by n places but in rotating way considering separatly A-Z and a-z that :
# Z, 1 means A not a or z 
# A, 26 means A not a or z 
# q, 27 means p not Q or P 
l = list(string)
n = int(input())
n = n%26
output = ""
l = [ord(i) for i in l]
for i in l:
    if i <= ord('Z'):
        jump = i + n
        if jump>ord('Z'):
            jump-=26
        output += chr(jump)
    else:
        jump = i + n
        if jump>ord('z'):
            jump-=26
        output += chr(jump)
print(output)

