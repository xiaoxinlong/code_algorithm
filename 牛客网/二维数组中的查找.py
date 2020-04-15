# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    @classmethod
    def Find(self, target, array):
        # write code here
        col, raw = 0, 0
        for col in range(0, len(array)):
            if array[col][0]==target:
                return True
            elif array[col][0]>target:
                break
        return False


if __name__=='__main__':
    list = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7]]
    print(list.index(2))
    print(Solution.Find(target=5, array=list))