def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


N = int(input())

max = 1

for i in range(N):
    for j in range(N):
        sum_of_digits = sum_digits(i ** j)
        if sum_of_digits > max:
            max = sum_of_digits

print(max)
