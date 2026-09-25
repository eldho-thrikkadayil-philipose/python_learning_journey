import random

secret = random.randint(1,20)
guess = -1

while guess != secret:
    guess = int(input('Guess a number between 1 and 20: '))

print('You have found it')