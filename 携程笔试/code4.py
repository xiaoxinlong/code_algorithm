



if __name__=='__main__':

    k = int(input())
    n = int(input())
    # weight = []
    # res = []
    weight = list(map(int,input().split()))
    gain = list(map(int,input().split()))
    mean_gain = (i/j for i,j in zip(weight,gain))

    dp = [[0]*(k+1) for _ in range(n+1)]

    if weight[0]<=k:
        for i in range(weight[0],k+1):
            dp[1][i] = gain[0]

    # print(dp[1])

    for i in range(2,n+1):
        for j in range(2,k+1):
            val = gain[i-1]
            w = weight[i-1]
            if j>=w:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+val)
            else:
                dp[i][j] = dp[i-1][j]
    # print(dp)

    i,j = n,k
    ans = []
    while i>0 and k>0:
        if dp[i][j]==dp[i-1][j]:
            i -= 1
            continue
        val = gain[i-1]
        w   = weight[i-1]
        if dp[i][j] == dp[i-1][j-w] + val:
            ans.append(i)
            i -= 1
            j -= w
        else:
            break

    # for i,ans_k in enumerate(ans):
    #     w = weight[ans_k-1]
    #     v = gain[ans_k-1]
    #     for temp_i, (temp_w,temp_v) in enumerate(zip(weight,gain)):
    #         if temp_i<ans_k-1 and temp_w==w and temp_v==v:
    #             # print(temp_i,i,ans_k)
    #             if temp_i+1 not in ans:
    #                 ans[i] = temp_i+1
    #             else:
    #                 temp_index = ans.index(temp_i+1)
    #                 ans[i] = temp_i + 1
    #                 ans[temp_index] = ans_k
    #             weight[temp_i] = -1
    #             weight[ans_k-1] = -1

    print(" ".join(map(str,ans)))
