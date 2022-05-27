import random

while True:
    n = random.randint(1,50)
    while True:
        ans = int(input('enter your guess:'))
        if ans == n:
            print('success!you win')
            break
        elif ans>n:
            print('too high:')
        elif ans==0:
            print('thank you')
            break
        else:
            print('too low:')

    con = int(input('do you want to continue the game 0:yes, 1:no'))
    if con==1:
        break