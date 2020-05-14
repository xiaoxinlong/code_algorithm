

from copy import deepcopy

if __name__=='__main__':

    k = int(input())
    n = int(input())
    # weight = []
    # res = []
    weight = list(map(int,input().split()))
    gain = list(map(int,input().split()))

    dp = [[0]*(k+1) for _ in range(n+1)]
    path = [[[] for ii in range(k+1)] for _ in range(n+1)]
    if weight[0]<=k:
        for i in range(weight[0],k+1):
            dp[1][i] = gain[0]
            path[1][i] = [1]

    for i in range(2,n+1):
        for j in range(2,k+1):
            val = gain[i-1]
            w = weight[i-1]
            if j>=w:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+val)
                if dp[i-1][j]>=dp[i-1][j-w]+val:
                    path[i][j] = deepcopy(path[i-1][j])
                else:
                    path[i][j] = deepcopy(path[i-1][j-w])
                    path[i][j].append(i)
            else:
                dp[i][j] = dp[i-1][j]
                path[i][j] = deepcopy(path[i-1][j])
    print(" ".join(map(str,path[-1][-1][::-1])))

