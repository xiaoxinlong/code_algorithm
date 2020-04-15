
input1 = input()
[n ,m] = [int(i) for i in input1.split()]

works = []
for i in range(n):
    input2 = input()
    [di, pi] = [int(j) for j in input2.split()]
    works.append([di ,pi ,pi])

works = sorted(works ,key=lambda x :x[0])
for i in range(n):
    if i== 0:
        continue
    works[i][2] = max(works[i - 1][2], works[i][1])

ans = []
input3 = input()
A = [int(i) for i in input3.split()]
for i in range(m):
    for j in range(n):
        if works[j][0] > A[i]:
            break
    if j == 0:
        ans.append(0)
    elif j == n - 1 and works[j][0] <= A[i]:
        ans.append(works[j][2])
    else:
        ans.append(works[j - 1][2])
print(works)
for i in ans:
    print(i)

