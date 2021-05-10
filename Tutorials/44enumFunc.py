a = ['Aloo', 'Bhindi', 'Momos', 'Chowmein', 'Fries']

i = 0 
for item in a:
    if i%2 != 0:    # ODD PLACES
        print(f"Jarvis please make : {item}")
    i+=1

j = 0
for item in a:
    if j%2 == 0:    # EVEN PLACES
        print(f"Jarvis please leave : {item}")
    j+=1

