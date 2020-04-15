


while True:
    nn = input()
    nn = nn.split()
    if nn=="":
        break
    n, w, h = int(nn[0]), int(nn[1]), int(nn[2])
    envelops = []
    for i in range(n):
        enve = input()
        enve = enve.split()
        # print(enve)
        w_i, h_i = int(enve[0]), int(enve[1])
        envelops.append([w_i, h_i, i])
    envelops = sorted(envelops, key=lambda x:x[0]*x[1])
    res_index = []
    w_pre, h_pre = w, h
    c = 0
    for temp_enve in envelops:
        [w_i, h_i, i]= temp_enve
        if w_i>w_pre and h_i>h_pre:
            res_index.append(i)
            w_pre = w_i
            h_pre = h_i
            c += 1
    if c==0:
        print(c)
    else:
        print(c)
        temp_str = ' '.join([str(i+1) for i in res_index])
        print(temp_str)


