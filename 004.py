def palindromes():
    l = []
    for i in range(100, 1000, 1):
        for j in range(100, 1000, 1):
            n = i * j
            num = str(n)
            if num == num[::-1] and len(num) == 6 and n not in l:
                l.append(n)
    l.sort()
    return l


T = int(input())
ll = palindromes()

for _ in range(T):
    N = int(input())
    maxi = ll[0]
    for i in range(len(ll)):
        if N > ll[i]:
            maxi = ll[i]
        else:
            break
    print(maxi)
