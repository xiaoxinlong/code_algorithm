class Solution:
    @classmethod
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j] == path[0]:
                    # print(i,j, matrix[i*cols+j])
                    if self.find(list(matrix),rows,cols,path[1:],i,j):
                        return True
        return False
    @classmethod
    def find(self,matrix,rows,cols,path,i,j):
        # print(matrix)
        if not path:
            return True
        temp = matrix[i*cols+j]
        matrix[i*cols+j]='0'
        if j+1<cols and matrix[i*cols+j+1]==path[0]:
            if self.find(matrix,rows,cols,path[1:],i,j+1):
                return True
        if j-1>=0 and matrix[i*cols+j-1]==path[0]:
            if self.find(matrix,rows,cols,path[1:],i,j-1):
                return True
        if i+1<rows and matrix[(i+1)*cols+j]==path[0]:
            if self.find(matrix,rows,cols,path[1:],i+1,j):
                return True
        if i-1>=0 and matrix[(i-1)*cols+j]==path[0]:
            if self.find(matrix,rows,cols,path[1:],i-1,j):
                return True
        matrix[i * cols + j] = temp
        return False

print(Solution.hasPath("ABCESFCSADEE",3,4,"FCCBASAD"))