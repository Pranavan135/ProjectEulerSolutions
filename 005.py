T = int(input())

for _ in range(T):
    N = int(input())
    l = []
    for i in range(2,N+1):
        j = 2
        while i != 1:
            counter = 0
            while i % j == 0:
                i //= j
                counter = counter + 1
            if l.count(j) < counter:
                x = counter - l.count(j)
                for _ in range(x):
                    l.append(j)
            j = j + 1

    summ = 1

    for m in range(len(l)):
        summ *= l[m]

    print(summ)
