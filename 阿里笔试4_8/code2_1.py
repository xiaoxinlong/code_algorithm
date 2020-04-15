import time


def solution(matrix, k, n):
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    max_re = [0]
    def dfs(i, j, re):
        for dire in directions:
            for step in range(1,k+1):
                new_i, new_j = i+step*dire[0],j+step*dire[1]
                if 0<=new_i<n and 0<=new_j<n:
                    if matrix[new_i][new_j]>matrix[i][j]:
                        max_re[0] = max(re+matrix[new_i][new_j],max_re[0])
                        dfs(new_i, new_j, re+matrix[new_i][new_j])
                else:
                    break
    dfs(0,0,matrix[0][0])
    return max_re[0]

# data = list(map(int,input().split()))
# T = data[0]

if __name__=='__main__':
    T = 1

    cur_time = time.time()
    for _ in range(T):
        # [n, k] = list(map(int,input().split()))
        # matrix = []
        # for i in range(n):
        #     matrix.append(list(map(int,input().split())))

        n = 6
        k = 2
        matrix = [[1, 2, 5, 3, 4, 6], [10, 11, 6, 3, 5, 9], [12, 12, 7, 16, 11, 10], [9, 17, 22, 12, 14, 23],
                  [14, 15, 16, 11, 15, 20], [22, 12, 23, 24, 21, 25]]
        print(solution(matrix,k,n))
    end_time = time.time()

    print("Cost_time :  ", end_time-cur_time)


