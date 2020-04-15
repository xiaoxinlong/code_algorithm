
array = [0,0,1,1,2,3,3,2,4,5]
temp = 0
for i in array:
    temp = temp^i
index = 1
while((temp&index)==0):
    index << 1
result1 = 0
result2 = 0
for i in array:
    if i&index==0:
        result1 = result1^i
    else:
        result2 = result2^i
print(result1, result2)