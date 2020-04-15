from collections import deque
class Solution:
    @classmethod
    def maxInWindows(self, num, size):
        # write code here
        queue, res, i = [], [], 0
        while size>0 and i<len(num):
            if len(queue)>0 and i-size+1>queue[0]:
                queue.pop(0)
            while len(queue)>0 and num[queue[-1]]<num[i]:
                queue.pop()
            print(queue,i)
            queue.append(i)
            if i>= size-1:
                res.append(num[queue[0]])
            i += 1
        return res

print(Solution.maxInWindows([2,3,4,2,6,2,5,1],3))