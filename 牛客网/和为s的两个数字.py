import sys
class Solution:
    @classmethod
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        length = len(array)
        res = []
        max_c = sys.maxsize
        for i in range(length):
            for j in range(i+1,length):
                print(i,j)
                if array[i]+array[j]==tsum:
                    if array[i]*array[j]<max_c:
                        res = [array[i],array[j]]
                        max_c = array[i] * array[j]
        return res

if __name__=='__main__':
    # print(Solution.FindNumbersWithSum([1,2,3,4,5,6],6))
    array = [1,2,3,4,5,6]
    tsum = 6
    low = 0
    high = len(array) - 1
    res = []

    while low < high:
        if array[low] + array[high] == tsum:
            res = [array[low], array[high]]
            low += 1
        elif array[low] + array[high] < tsum:
            low += 1
        else:
            high -= 1
    print(res)