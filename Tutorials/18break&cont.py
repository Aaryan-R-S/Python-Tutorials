i = 0

# Forever loop
while (True) :
    if (i<=10) :
        i = i+1
        continue #don't leave the loop & don't read the code written in loop (after this)
    print(i, end=' ')
    i = i+1
    if (i==45) :
        break   #leave the loop without reading code written in loop (after this)

print(i)
print('Stopped!')