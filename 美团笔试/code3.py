
import pdb

while True:

    nn = input()
    if nn=="":
        break
    nn = [int(i) for i in nn.split()]
    [n, k, m] = nn
    mm = input().split()
    mm= [int(i) for i in mm]
    [p, q] = mm
    time = input()
    time = time.split()
    time = [int(i) for i in time]
    time = sorted(time)
    all_time = sum(time)
    all_time_re = (p*k+q)/float(all_time)
    time_re = [p/float(i) for i in time]
    res = m
    t_count = 0
    # while(res>0):
    count = [0 for __ in range(k)]
    # pdb.set_trace()
    ans = 0
    if all_time_re>max(time_re) and res>=all_time:
        temp = p*k + q
        num = min(int(res/all_time), n)
        res -= all_time*num
        ans += temp*num
        for i in count:
            i += num
    for i, temp_time in enumerate(time):
        temp_time_count = count[i]
        res_count = n - temp_time_count
        res_count = min(res_count, int(res/temp_time))
        res -= res_count*temp_time
        ans += res_count*p
        count[i] += res_count
    print(ans)








