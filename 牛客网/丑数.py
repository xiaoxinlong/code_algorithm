# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index < 7:
            return index
        queue = [1]
        t2, t3, t5 = 0, 0, 0
        for i in range(1, index):
            temp = min(queue[t2]*2, queue[t3]*3, queue[t5]*5)
            # print(i, temp)
            queue.append(temp)
            if temp==queue[t2]*2: t2 += 1     # 如果更新的是乘2，对应因子2的位置要挪一位，保证下一位置乘2大于最后一位，且是乘二最小的丑数
            if temp==queue[t3]*3: t3 += 1
            if temp==queue[t5]*5: t5 += 1
        return queue[-1]

if __name__=="__main__":
    Num_Solution = Solution()
    num = Num_Solution.GetUglyNumber_Solution(index=7)
    print(num)