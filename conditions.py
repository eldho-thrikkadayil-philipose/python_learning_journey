a = int(input('input of a: '))

if a < 0:
    print('You entered a neagtive number.')
elif a > 0:
    print('You entered a positive number')
else:
    print('You entered zero')

print ('The number is', ('odd.' if a % 2 == 1 else 'even.'))