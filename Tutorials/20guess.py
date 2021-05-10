print(' ')
print('Welcome to Guess the Number Game!\n')
print('The number is between 1 to 100\n')
num = 10
guessesLeft = 4
print("No of Turns left :", guessesLeft)

while(guessesLeft>=0) :
    inp = int(input('Guess the number : '))

    if (inp==num):
        print(" ")
        print('Congarts! You WON the Game with no of turns left :', guessesLeft,'\n')
        break

    if (guessesLeft==0):
        print('You LOSE!\n')
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

