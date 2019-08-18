# brute force way of writing the program, still passes all the test cases.

def power_sum(num, n):
    num_str = str(num)
    s = 0
    for i in range(len(num_str)):
        s += pow(ord(num_str[i]) - 48, n)

    return s == num


N = int(input())

n_th_power = 0

for i in range(2, 10**6): # upper bound can be reduced
    if power_sum(i, N):
        n_th_power += i

print(n_th_power)