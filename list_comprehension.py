cube = [i**3 for i in range (1, 6)]
print('cube: ' , cube)

l1 = [ i ** 2 for i in range(1,11)]
l2 = [sus * 3 for sus in l1]

print ('l2: ', l2)

l3 = [23, 56, 5, 7]

lsum = [a+b for a, b in zip(l3,l2) ]
print('lsum: ', lsum)

#if the lists have different length, using 'len()' can raise an IndexError
#we will use 'zip()' instead