import random
print(' ')
print('Welcome to Snake, Water & Gun World!')
start = input('\nEnter 1 to start the Game & Any other Key to Quit! : ')

cScore = 0
yScore = 0
lst = ['S', 'W', 'G']
t = False

if start=='1':
    i = 0
    while i<10:
        if i == 0:
            print(f"\nRound : {i+1}/10")

        computer = random.choice(lst)
        player = input("Enter 'S' for Snake, 'W' for Water , 'G' for Gun and 'Q' to Quit : ")

        if player == 'S' or player == 'W' or player == 'G':
            t = True
            i+=1
            if player == 'S' and computer == 'G':
                cScore+=1
                print(f"\nComputer : {cScore} [GUN]\nYou : {yScore} [SNAKE]")
                print(f"\nRound : {i+1}/10")
            elif player == 'S' and computer == 'W':
                yScore+=1
                print(f"\nComputer : {cScore} [WATER]\nYou : {yScore} [SNAKE]")
                print(f"\nRound : {i+1}/10")
            elif player == 'W' and computer == 'G':
                yScore+=1
                print(f"\nComputer : {cScore} [GUN]\nYou : {yScore} [WATER]")
                print(f"\nRound : {i+1}/10")
            elif player == 'W' and computer == 'S':
                cScore+=1
                print(f"\nComputer : {cScore} [SNAKE]\nYou : {yScore} [WATER]")
                print(f"\nRound : {i+1}/10")
            elif player == 'G' and computer == 'S':
                yScore+=1
                print(f"\nComputer : {cScore} [SNAKE]\nYou : {yScore} [GUN]")
                print(f"\nRound : {i+1}/10")
            elif player == 'G' and computer == 'W':
                cScore+=1
                print(f"\nComputer : {cScore} [WATER]\nYou : {yScore} [GUN]")
                print(f"\nRound : {i+1}/10")
            else :
                if player == 'S' :
                    print(f"\nComputer : {cScore} [SNAKE]\nYou : {yScore} [SNAKE]")
                    print(f"\nRound : {i+1}/10")

                elif player == 'W' :
                    print(f"\nComputer : {cScore} [WATER]\nYou : {yScore} [WATER]")
                    print(f"\nRound : {i+1}/10")

                else :
                    print(f"\nComputer : {cScore} [GUN]\nYou : {yScore} [GUN]")
                    print(f"\nRound : {i+1}/10")

            
        elif player == 'Q':
            break       
        else:
            print('\nInvalid Input!')


print('\nGame Ended!')
if t==True :
    print(f'\nComputer Score : {cScore}')
    print(f'Your Score : {yScore}')
    if cScore > yScore:
        print('COMPUTER WON!')
    elif cScore<yScore:
        print('YOU WON!')
    else:
        print("IT'S A TIE !")
print(' ')