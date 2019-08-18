def change_num_to_base_k(num, k):
    numeric_str = ''

    while num >= k:
        numeric_str = str(num % k) + numeric_str
        num //= k

    numeric_str = str(num % k) + numeric_str

    return numeric_str


def check_palindrome(num):
    return num == num[::-1]


nk = input().split()
N, K = int(nk[0]), int(nk[1])

s = 0
for i in range(1, N):
    if check_palindrome(str(i)) and check_palindrome(change_num_to_base_k(i, K)):
        s += i

print(s)
