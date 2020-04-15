


while True:
    nn = input()
    if nn=="":
        break
    nn = nn.split()
    mm_1 = input()
    mm_1 = mm_1.split()
    mm_1 = [int(i) for i in mm_1]
    mm_1 = sorted(mm_1)
    temp_1 = sum(mm_1[-3:])

    mm_2 = input()
    mm_2 = mm_2.split()
    mm_2 = [int(i) for i in mm_2]
    mm_2 = sorted(mm_2)
    temp_2 = sum(mm_2[-3:])

    if temp_1>temp_2:
        print(temp_1)
    else:
        print(temp_2)
