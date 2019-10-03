def primes_sieve(limit):
    a = [True] * (limit + 1)
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            for n in range(2 * i, limit, i):
                a[n] = False

    return a


def is_prime(n):
    if n == 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def is_circular_prime(number, a, N):
    size = len(str(number)) - 1
    for k in range(size):
        number = int(number / 10 + (number % 10) * (10 ** size))
        if number > N:
            if not is_prime(number):
                return False
        elif not a[number]:
            return False
    return True


N = int(input())

primes = primes_sieve(N)
s = 0
for i in range(N):
    if primes[i]:
        if is_circular_prime(i, primes, N):
            s += i

print(s)
