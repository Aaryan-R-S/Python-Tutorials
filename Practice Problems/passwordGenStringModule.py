import string
import random

# --------- 1 -----------
s1 = string.ascii_lowercase          # or give abcdefgh......
# print(list(s1))
# print(s1)
s2 = string.ascii_uppercase
# print(s2)
s3 = string.digits
# print(s3)
s4 = string.punctuation
# print(s4)

# --------- 2 -----------
s = [] 
s.extend(list(s1))    # [append] give the element to list while [extend] give list 
s.extend(list(s2))    # but we have to make string of s's to list using list()
s.extend(list(s3))
s.extend(list(s4))
# print(s)
random.shuffle(s)       # shuffles a list
# print(s)

# --------- 3 -----------
lenPwd = int(input("\nEnter Password Length :\n "))
print("\nYour Pasword is :",end=" ")
print("".join(s[0:lenPwd]))
# --OR--
print("\nYour Pasword is :",end=" ")
print("".join(random.sample(s,lenPwd)))        # list, no of values
print("")
