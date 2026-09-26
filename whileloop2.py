import random

secret = random.randint(1,20)
guess = -1

while guess != secret:
    guess = int(input('Guess a number between 1 and 20, press zero to give up: \n'))
    if guess == 0:
        print('The game is terminated')
        break
else:
    print('Your have found it')