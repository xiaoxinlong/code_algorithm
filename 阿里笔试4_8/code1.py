

# T
data = list(map(int,input().split()))
T = data[0]

for _ in range(T):
    [n,m,a,b] = list(map(int,input().split()))
    if b==1:
        print(min(n//a,m))
        continue
    if n<a:
        print(0)
        continue
    elif n==a:
        print(min(b,m))
        continue
    if n*b>=m*a:
        print(m)
    else:
        print(n*b//a)

