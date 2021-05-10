import os
from os import path 

def pretify(path, file, format):

    os.chdir(path)
    files = os.listdir(path)

    with open(file) as e:
        fileList = e.read().split("\n")

    i = 1

    for f in files:
        if f not in fileList:
            os.rename(f, f.capitalize())
        
        if os.path.splitext(f)[1] == format:
            os.rename(f, f"{i}{format}")
            i+=1

p = input("Enter Full Path of Directory you want to PRETIFY :\n ")
f = input("Enter Relative Path of File you want to check before PRETIFY :\n ")
e = input("Enter Format of files you want to PRETIFY :\n ")

pretify(p, f, e)
