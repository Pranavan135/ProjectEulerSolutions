def primes_sieve(bound):
    a = [True] * bound
    a[0] = a[1] = False
    primes_list = []
    for (i, isprime) in enumerate(a):
        if isprime:
            primes_list.append(i)
            for n in range(2 * i, bound, i):
                a[n] = False

    return primes_list


limit = 3162

LIMIT_L = 10 ** 7

primes = primes_sieve(limit)

s = set()

for i in range(len(primes)):
    val1 = primes[i] ** 2
    if val1 > LIMIT_L:
        break
    for j in range(len(primes)):
        val2 = val1 + primes[j] ** 3
        if val2 > LIMIT_L:
            break
        for k in range(len(primes)):
            val3 = val2 + primes[k] ** 4
            if val3 > LIMIT_L:
                break
            else:
                s.add(val3)

l = sorted(s)

results = [0] * (LIMIT_L + 1)
counter = 0
for i in range(1, len(results)):
    if counter < len(l) and l[counter] == i:
        counter = counter + 1
    results[i] = counter

T = int(input())

for _ in range(T):
    print(results[int(input())])
