import time

from copy import deepcopy


def solution(matrix, k, n):
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    dp = [[-1]*n for _ in range(n)]
    def dfs(i, j):
        flag = 0
        re = matrix[i][j]
        temp_max = matrix[i][j]
        for dire in directions:
            for step in range(1,k+1):
                new_i, new_j = i+step*dire[0],j+step*dire[1]
                if 0<=new_i<n and 0<=new_j<n:
                    if matrix[new_i][new_j]>matrix[i][j]:
                        if dp[new_i][new_j]==-1:
                            temp_ans = re + dfs(new_i, new_j)
                        else:
                            temp_ans = re + dp[new_i][new_j]
                        temp_max = max(temp_max, temp_ans)
                else:
                    break
        dp[i][j] = temp_max
        return temp_max
    dfs(0,0)
    print(dp)
    return dp[0][0]


if __name__=='__main__':
    T = 1
    cur_time = time.time()
    for _ in range(T):
        n = 6
        k = 2
        matrix = [[1,2,5,3,4,6],[10,11,6,3,5,9],[12,12,7,16,11,10],[9,17,22,12,14,23],[14,15,16,11,15,20],[22,12,23,24,21,25]]
        print(solution(matrix,k,n))
    end_time = time.time()

    print("Cost_time :  ", end_time-cur_time)



