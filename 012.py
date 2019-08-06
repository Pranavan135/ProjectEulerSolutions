def primes_sieve(limit):
    a = [True] * limit  # Initialize the primality list
    a[0] = a[1] = False
    l = []

    for (i, isprime) in enumerate(a):
        if isprime:
            l.append(i)
            for n in range(2 * i, limit, i):  # Mark factors non-prime
                a[n] = False

    return l, a


def count_factors(num, primes):
    c = {}
    j = 0
    while num != 1:
        count = 0
        while num % primes[j] == 0:
            num //= primes[j]
            count = count + 1

        if count > 0:
            c.update({primes[j]: count})

        j = j + 1

    return c


T = int(input())
l, _ = primes_sieve((10 ** 5))
N = 1000
x = {1: 1}
i = 2
factors = 1
while factors <= N:
    p, q = {}, {}
    if i % 2 == 0:
        p, q = count_factors(i // 2, l), count_factors(i + 1, l)
    else:
        p, q = count_factors(i, l), count_factors((i + 1) // 2, l)

    r = p

    for element in q:
        if element in r:
            r.update({element: max(r[element], q[element])})
        else:
            r.update({element: q[element]})

    f = 1

    for element in r:
        f *= (r[element] + 1)
    factors = f
    x.update({i: f})
    i = i + 1

for _ in range(T):
    N = int(input())
    i = 1

    while x[i] <= N:
        i = i + 1

    print(i * (i + 1) // 2)
