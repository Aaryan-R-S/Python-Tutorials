# ------------------1---------------
import random
import pickle
import os

os.chdir('D:\My Files\Complete Python Course\Problems')

s = "abcdefghijklmnopqrstuvwxyz1234567890-_=+!@#$%^&*()~{[}]:;'|><.,/?ASDFGHJKLQWERTYUIOPZXCVBNM"


# ------------------2---------------
sT = tuple(s)

def randomize():
    sL = list(s)
    random.shuffle(sL)
        
    def listToString(s): 	
    	str1 = "" 
    	for ele in s: 
    		str1 += ele 
    	return str1 

    code = listToString(sL)

    f = open('securePwdCode.pkl', 'wb')
    pickle.dump(code, f)   
    f.close()

# ------------------3---------------
def encrypt(p):
    f = open('securePwdCode.pkl', 'rb')
    codeE = tuple(pickle.load(f)) 

    codify = tuple(zip(sT, codeE))

    for i in range(len(p)):
        for x,y in codify:
            if x==p[i]:
                p = p.replace(x, y)
                break
    return p

def decrypt(p):
    f = open('securePwdCode.pkl', 'rb')
    codeE = tuple(pickle.load(f)) 

    codify = tuple(zip(sT, codeE))

    for i in range(len(p)):
        for x,y in codify:
            if y==p[i]:
                p = p.replace(y, x)
                break
    return p


# ------------------4---------------
if __name__ == "__main__":
    if not os.path.isfile('securePwdCode.pkl'):
        randomize()

    print("\nWelcome to PassWord Encrypt & Decrypt!")
    while True:
        print("\nPress 'e' to Encrypt, 'd' to Decrypt, 'r' to change Encryption Pattern & 'c' to exit :\n")
        inp = input()
        if inp == 'e':
            pwd = input("\nEnter your Password which is to be Encrypted:\n ")
            e = encrypt(pwd)
            print("\nYour Encrypted Password is =>",'\n',e)


        elif inp == 'd':
            pwd = input("\nEnter your Password which is to be Decrypted:\n ")
            d = decrypt(pwd)
            print("\nYour Decrypted Password is =>",'\n',d)

        elif inp == 'r':
            randomize()

        elif inp == 'c':
            exit()
        

