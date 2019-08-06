T = int(input())
for a0 in range(T):
    n = int(input())
    maximum = -1
    N = n // 3

    for i in range(N):
        a = (i+1)
        b = n*(n-2*a)/(2*(n-a))
        c = n - a - b
        if b % 1 != 0:
            continue
        if a*b*c > maximum:
            maximum = a*b*c
    print(int(maximum))