# -*- coding:utf-8 -*-
class Solution:
    @classmethod
    def movingCount(self, threshold, rows, cols):
        # write code here
        global ans
        ans = 0
        visited = [[0]*cols for _ in range(rows)]
        def bfs(i,j):
            global ans
            visited[i][j]=1
            temp = str(i)+str(j)
            temp = sum([int(i) for i in temp])

            if temp>threshold:
                print(i,j,temp)
                return
            print(i, j, temp)
            ans += 1
            if i+1<rows and visited[i+1][j]==0:
                bfs(i+1,j)
            if i-1>=0 and visited[i-1][j]==0:
                bfs(i-1,j)
            if j+1<cols and visited[i][j+1]==0:
                bfs(i,j+1)
            if j-1>=0 and visited[i][j-1]==0:
                bfs(i,j-1)
        bfs(0,0)
        return ans

print(Solution.movingCount(threshold=5,rows=10,cols=10))