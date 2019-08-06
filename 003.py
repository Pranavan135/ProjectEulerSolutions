import math

T = int(input())

for j in range(T):
    x = int(input())
    N = x
    largest_factor = 1
    i = 2
    k = int(math.sqrt(x)) + 1

    while x != 1 and i < k:
        while x % i == 0:
            x //= i
            largest_factor = i
        i = i + 1

    if x > largest_factor:
        print(x)
    else:
        print(largest_factor)
