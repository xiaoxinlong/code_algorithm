
directions = [[0,1],[0,-1],[1,0],[-1,0]]
def solution(data):
    m = len(data)
    n = len(data[0])
    global max_ans
    max_ans = 0
    visited = [[False]*n for _ in range(m)]

    def dfs(i,j,res):
        global max_ans
        flag = 1
        for d in directions:
            new_i,new_j = i+d[0], j+d[1]
            if 0<=new_i<m and 0<=new_j<n and data[new_i][new_j]!=0 and visited[new_i][new_j]==False:
                flag = 0
                visited[new_i][new_j] = True
                dfs(new_i,new_j,res+data[new_i][new_j])
                visited[new_i][new_j] = False
        if flag==1:
            max_ans = max(res,max_ans)
        return

    for i in range(m):
        for j in range(n):
            if data[i][j]!=0:
                visited[i][j] = True
                dfs(i,j,data[i][j])
                visited[i][j] = False

    return max_ans

if __name__=="__main__":
    n = int(input())
    data = []
    for _ in range(n):
        temp_data = list(map(int, input().split()))
        data.append(temp_data)
    # data = [[0, 6, 0, 0, 0], [5, 8, 7, 1, 0], [0, 9, 0, 1, 0], [0, 1, 0, 0, 1]]
    print(solution(data))