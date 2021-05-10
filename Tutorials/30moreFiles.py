openFile = open('Tuts/30.txt')

#Check where is file pointer -- 
print(openFile.tell())
print(openFile.readline())

openFile.seek(0) # change file pointer!
print(openFile.tell())
print(openFile.readline())

openFile.close()