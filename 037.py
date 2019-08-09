def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            for n in range(i * i, limit, i):
                a[n] = False
    return a


def truncatable(n, a):
    if not a[n]:
        return False
    num1 = str(n)
    num2 = str(n)

    while num1:
        if not a[int(num1)] or not a[int(num2)]:
            return False
        num1 = num1[:len(num1) - 1]
        num2 = num2[1:]
    return True


N = int(input())
a = primes_sieve(N)

summation = 0

for i in range(10, N):
    if truncatable(i, a):
        summation = summation + i

print(summation)
