T = int(input())

MAX = 4*(10**16)
MIN = 10

l = []
x = 1
y = 1
while True:
    z = x + y
    if z % 2 == 0:
        l.append(z)
    x, y = y, z
    if z > MAX:
        break

suml = [2]

for i in range(T):
    N = int(input())
    s = 0
    for i in range(len(l)):
        if l[i] > N:
            break
        else:
            s = s + l[i]
    print(s)
