def primes_sieve2(limit):
    a = [True] * limit
    factors = [0] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            for n in range(2 * i, limit, i):
                a[n] = False
                factors[n] = factors[n] + 1

    return factors


numbers = numbers = list(map(int, input().split()))

N = numbers[0]
K = numbers[1]

flag = [False] * (N + K)

prime_factors = primes_sieve2(N + K)

for i in range(2, N + K):
    flag[i] = (prime_factors[i] == K)

for i in range(2, N + 1):
    pri = True
    for j in range(i, i + K):
        pri = flag[j]
        if not pri:
            break
    if pri:
        print(i)
