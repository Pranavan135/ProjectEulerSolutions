numbers = list(map(int, input().split()))

N = numbers[0]
a = numbers[1]
b = numbers[2]

t_p =[1, 210, 40755, 7906276, 1533776805, 297544793910, 57722156241751]
p_h = [1, 40755, 1533776805, 57722156241751]


if a == 3:
    for i in range(len(t_p)):
        if t_p[i] < N:
            print(t_p[i])
        else:
            break


if a == 5:
    for i in range(len(p_h)):
        if p_h[i] < N:
            print(p_h[i])
        else:
            break
