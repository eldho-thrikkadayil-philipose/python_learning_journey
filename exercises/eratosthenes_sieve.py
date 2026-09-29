n = int(input("Enter n: "))

is_prime = [True]*(n+1)

is_prime[0] = False
is_prime[1] = False

for p in range(2, n+1):
    if is_prime[p]:
        for multiple in range(2*p, n+1, p):
            is_prime[multiple] = False

for i in range(2, n+1):
    if is_prime[i]:
        print(i)


