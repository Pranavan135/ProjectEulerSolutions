MAX = 5 * (10 ** 6)
final_count_list = [0] * (MAX + 1)
desired = [0] * (MAX + 1)
temp = [[3, 4, 5]]

while len(temp) != 0:
    a, b, c = temp.pop()
    s = a + b + c
    current = s
    while current <= MAX:
        final_count_list[current] += 1
        current += s
    a1, b1, c1 = a - 2 * b + 2 * c, 2 * a - b + 2 * c, 2 * a - 2 * b + 3 * c
    a2, b2, c2 = a + 2 * b + 2 * c, 2 * a + b + 2 * c, 2 * a + 2 * b + 3 * c
    a3, b3, c3 = (-1) * a + 2 * b + 2 * c, (-2) * a + b + 2 * c, (-2) * a + 2 * b + 3 * c

    if a1 + b1 + c1 <= MAX:
        temp.append([a1, b1, c1])
    if a2 + b2 + c2 <= MAX:
        temp.append([a2, b2, c2])
    if a3 + b3 + c3 <= MAX:
        temp.append([a3, b3, c3])

index = 12
current = 0

while index <= MAX:
    if final_count_list[index] == 1:
        current += 1
    desired[index] = current
    index += 1

T = int(input())

for _ in range(T):
    print(desired[int(input())])
