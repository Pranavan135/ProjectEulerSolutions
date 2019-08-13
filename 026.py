# from datetime import datetime as dt

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


N = 10000

largest_cycle_below = [0] * N

largest_cycle_below[3] = 3
largest_cycle_below[4] = 3
largest_cycle_below[5] = 3
largest_cycle_below[6] = 3

# a = dt.now()
_, primes = primes_sieve(N)
# b = dt.now()

# print((b-a).total_seconds())

# a = dt.now()
for i in range(7, N):
    prev = largest_cycle_below[i] = largest_cycle_below[i - 1]
    if primes[i]:
        for j in range(1, i):
            big_no_remainder = pow(10, j, i)  # very useful and efficient remainder operation in python
            if big_no_remainder == 1:
                if prev < j:
                    largest_cycle_below[i] = i
                break

# b = dt.now()

# print((b-a).total_seconds())


T = int(input())

for _ in range(T):
    print(largest_cycle_below[int(input()) - 1])
