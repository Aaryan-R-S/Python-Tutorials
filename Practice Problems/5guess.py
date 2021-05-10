import random
print(' ')
print('Welcome to Guess the Number Game!\n')
a = int(input("Enter Lower bound : "))
b = int(input("Enter Upper bound : "))
print(f'The number is between {a} to {b}\n')

print("Player 1 Turns!\n") 
num = random.randint(a,b)
guessesLeft = 10
print("No of Turns left :", guessesLeft)

while(guessesLeft>=0) :
    inp = int(input('Guess the number : '))

    if (inp==num):
        print(" ")
        print('You Complete the Game with no of turns left :', guessesLeft,'\n')
        break

    if (guessesLeft==0):
        print('Your Game over!\n')
        break

    elif (inp<num):
        print('No...Go HIGH!\n')
        guessesLeft = guessesLeft-1
        print("No of Turns left :", guessesLeft)
        continue

    elif (inp>num):
        print('No...Go LOW!\n')
        guessesLeft = guessesLeft-1
        print("No of Turns left :", guessesLeft)
        continue

    else :
        print('Check your Input!\n')

j = guessesLeft

print("Player 2 Turns!\n")
num = random.randint(a,b)
guessesLeft = 10
print("No of Turns left :", guessesLeft)

while(guessesLeft>=0) :
    inp = int(input('Guess the number : '))

    if (inp==num):
        print(" ")
        print('You Complete the Game with no of turns left :', guessesLeft,'\n')
        break

    if (guessesLeft==0):
        print('Your Game over!\n')
        break

    elif (inp<num):
        print('No...Go HIGH!\n')
        guessesLeft = guessesLeft-1
        print("No of Turns left :", guessesLeft)
        continue

    elif (inp>num):
        print('No...Go LOW!\n')
        guessesLeft = guessesLeft-1
        print("No of Turns left :", guessesLeft)
        continue

    else :
        print('Check your Input!\n')

k = guessesLeft

if j==k:
    print("It's a TIE !")
elif j<k:
    print("Player 2 Wins !")
elif j>k:
    print("Player 1 Wins !")
