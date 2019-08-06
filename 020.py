def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


T = int(input())
l = [0] * 1001
l[0] = 1
fact = 1
for i in range(1,1001):
    fact *= i
    l[i] = sum_digits(fact)

for _ in range(T):
    N = int(input())
    print(l[N])
