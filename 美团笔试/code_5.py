
import pdb

def ans(L):

    dp1 = [L[0]]
    for i, item in enumerate(L[1:]):

        if dp1[-1]<=item:
            dp1.append(item)
            continue
        for j, j_item in enumerate(dp1):
            if j_item > item:
                break
        dp1[j] = item
        print(dp1)
    return len(dp1)



if __name__=="__main__":
    data = "0101010101010010111000000010101"
    data = [int(i) for i in data]
    print(ans(data))

    L = [2,1,5,3,6,4,8,9,7]
    print(ans(L))

    # while True:
    #     nn = input()
    #     if nn == "":
    #         break
    #     nn = nn.split()
    #     nn = [int(i) for i in nn]
    #     [length, count] = nn
    #     temp_list = input()
    #     temp_list = [int(i) for i in temp_list]
    #     for _ in range(count):
    #         temp_input = input()
    #         if len(temp_input)==1:
    #             print(ans(temp_list))
    #         else:
    #             temp_input = temp_input.split()
    #             for i in range(int(temp_input[1])-1,int(temp_input[2])):
    #                 temp_list[i] = 1-temp_list[i]



