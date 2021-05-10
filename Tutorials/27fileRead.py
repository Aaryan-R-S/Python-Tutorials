openFile = open('Tuts/27.txt', "rt")  # read + text mode
# openFile = open('Tuts/25.txt', "rb")  # read + binary mode

# Print all line by line (dont read file before it) --
# for line in openFile:
#     print(line)

# READING--
readFile = openFile.read()
print(readFile)
#         OR
# readLine = openFile.readline()
# print(readLine)
# readLine = openFile.readline()
# print(readLine)
# readLine = openFile.readline()
# print(readLine)
#         OR
# readLines = openFile.readlines()
# print(readLines)


# Print all characters in new line --
# for char in readFile :
#     print(char)

# STEP BY STEP READ 5 characters-- 
# readFile = openFile.read(10)
# print(readFile)
# readFile = openFile.read(10)
# print(readFile)

openFile.close()