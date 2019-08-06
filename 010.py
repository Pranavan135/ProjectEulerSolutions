def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False
    l = []

    for (i, isprime) in enumerate(a):
        if isprime:
            l.append(i)
            for n in range(2*i, limit, i):     # Mark factors non-prime
                a[n] = False

    return l, a

T = int(input())

_, aa = primes_sieve(10**6)
sum_a = [0] * (10**6)
sum_m = 0

for i in range(10**6):
    if aa[i]:
        sum_m += i

    sum_a[i] = sum_m

for _ in range(T):
    N = int(input())
    print(sum_a[N])