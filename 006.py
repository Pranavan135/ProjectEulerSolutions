T = int(input())

for _ in range(T):
    n = int(input())
    s = (n*(n+1)//2)**2 - n*(n+1)*(2*n+1)//6
    print(s)