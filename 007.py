def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False
    l = []

    for (i, isprime) in enumerate(a):
        if isprime:
            l.append(i)
            for n in range(2*i, limit, i):     # Mark factors non-prime
                a[n] = False

    return l

T = int(input())

ll = primes_sieve(105*(10**3))

for _ in range(T):
    N = int(input())
    print(ll[N-1])