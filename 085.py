from operator import itemgetter

limit = 2 * (10 ** 6)
des_res = [0] * (limit + 1)
T = int(input())

d = {}

for i in range(1, 53):
    j = i
    while i * j * (i + 1) * (j + 1) // 4 <= limit:
        mul = (i, j)
        val = i * j * (i + 1) * (j + 1) // 4
        j = j + 1
        d[mul] = val

l_t = sorted(d.items(), key=itemgetter(1))

d_l = []
a_l = []

idx = 0
while idx < len(l_t) - 1:
    if l_t[idx][1] < l_t[idx + 1][1]:
        d_l.append(l_t[idx][1])
        a_l.append(l_t[idx][0][0] * l_t[idx][0][1])
    else:
        current = l_t[idx][0][0] * l_t[idx][0][1]
        while l_t[idx][1] == l_t[idx + 1][1]:
            idx = idx + 1
            if current < l_t[idx][0][0] * l_t[idx][0][1]:
                current = l_t[idx][0][0] * l_t[idx][0][1]
        d_l.append(l_t[idx][1])
        a_l.append(current)
    idx = idx + 1

d_l.append(l_t[idx][1])
a_l.append(l_t[idx][0][0] * l_t[idx][0][1])

idx = 0
for i in range(1, len(des_res)):
    if idx == len(d_l) - 1:
        des_res[i] = a_l[idx]
    else:
        val = abs(d_l[idx] - i) - abs(d_l[idx + 1] - i)
        if val < 0:
            des_res[i] = a_l[idx]
        elif val == 0:
            des_res[i] = max(a_l[idx], a_l[idx + 1])
        else:
            des_res[i] = a_l[idx + 1]
            idx = idx + 1

for _ in range(T):
    N = int(input())
    print(des_res[N])
