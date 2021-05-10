# -------------------- Inputs ---------------
while True:
    try:
        inp = int(input("Enter Age or Year of Birth :\n "))
        year = int(input("Enter the Year for which You want to Know your Age :\n "))    
    except Exception as e:
        print("[Invalid Entry] Please enter an integer : ", e)
    else:
        if inp>=0 and year>=0:
            break
        else:
            print("[Invalid Entry] Please enter a number greater than 0")

# -------------------- Calculate ---------------
p = False
age = 0

if inp>=0 and inp<=100:
    age = inp+(year-2020)
    p = True

elif inp<=0 or inp>2020:
    print("You aren't Born yet!")

elif inp>=1920 and inp<=2020:
    age = year-inp
    p = True

elif inp<1920 and inp>100:
    print("You seemed to be Oldest person Right Now!")

# -------------------- Result ---------------
if p and age>=0 and age<=100:
    print(f"Your Age in {year} would be {age}")
elif age<0:
    print("You weren't Born yet!")
elif age>100:
    print("You seems to be Oldest person That Time!")


