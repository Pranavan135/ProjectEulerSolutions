def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False
    l = []

    for (i, isprime) in enumerate(a):
        if isprime:
            l.append(i)
            for n in range(2 * i, limit, i):
                a[n] = False

    return l, a


N = int(input())

l, _ = primes_sieve(N + 1)
_, primes = primes_sieve(150000)

A, B, MAX = 0, 0, 0
for a in range(-N, N + 1):
    for c in range(-len(l) + 1, len(l)):
        b = l[c] if c >= 0 else -1 * l[abs(c)]
        counter = 0
        i = counter * counter + a * counter + b
        while i >= 0 and primes[i]:
            counter += 1
            i = counter * counter + a * counter + b

        if counter > MAX:
            MAX = counter
            A, B = a, b

print(A, B)
