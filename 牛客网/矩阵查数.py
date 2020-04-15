
input1 = input().split()
m = int(input1[0])
n = int(input1[1])

in_list = []
for i in range(m):
    temp_input = input().split()
    print(temp_input)
    temp_input = [int(t) for t in temp_input]
    in_list.append(temp_input)

a = set()
a.update()
target = input().split()
target = int(target[0])

row = m- 1
col = 0
flag = 0
while (row >= 0 and col < n):
    if in_list[row][col] > target:
        row -= 1
    elif in_list[row][col] < target:
        col += 1
    else:
        print('true')
        flag = 1
        break
if not flag:
    print('false')




