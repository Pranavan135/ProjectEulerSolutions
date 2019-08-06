T = int(input())

MIN, MAX = 10, 4*(10**16)

l = []
x, y = 1, 1

while True:
    z = x + y
    if z % 2 == 0:
        l.append(z)
    x, y = y, z
    if z > MAX:
        break


for i in range(T):
    N = int(input())
    s = 0
    for i in range(len(l)):
        if l[i] > N:
            break
        else:
            s = s + l[i]
    print(s)