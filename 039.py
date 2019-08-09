def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


T = int(input())

freq = [0] * 10000000
b = [0] * 10000000

for m in range(2, 1201):
    for n in range(1, m):
        if (m + n) % 2 != 0 and gcd(m, n) == 1:
            perimeter = 2 * m * (m + n)
            for k in range(1, 100000000):
                if k * perimeter > 5000000:
                    break
                else:
                    freq[k * perimeter] = freq[k * perimeter] + 1

for i in range(2, 5000000):
    if freq[i] > freq[b[i - 1]]:
        b[i] = i
    else:
        b[i] = b[i - 1]

for i in range(T):
    N = int(input())
    print(b[N])
