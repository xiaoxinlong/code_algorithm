tsum = 100
low = 1
hight = 2
result = []
while low<hight:
    cur = (hight-low+1)*(hight+low)/2
    if cur==tsum:
        result.append([i for i in range(low,hight+1)])
        low += 1
    elif cur<tsum:
        hight += 1
    else:
        low += 1
print(result)
