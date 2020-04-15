# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or len(pushV) != len(popV):
            return False
        stack = []
        stack.append(pushV.pop(0))

        while True:
            while popV[0] != stack[-1] and len(pushV)>0:
                stack.append(pushV.pop(0))
            if stack[-1]!=popV[0]:
                return False
            # print(stack)
            while len(popV)>0 and len(stack)>0 and popV[0] == stack[-1]:
                popV.pop(0)
                stack.pop()
            if len(popV)==0:
                return True


if __name__=='__main__':
    s = Solution()
    pre = [1,2,3,4,5]
    order = [4,3,5,1,2]  # [4 5 3 2 1]
    # order = [4, 5, 3, 2, 1]
    print(s.IsPopOrder(pre,order))