# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.HasSubtree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def HasSubtree2(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val == pRoot2.val:
            return self.HasSubtree2(pRoot1.left, pRoot2.left) and self.HasSubtree2(pRoot1.right, pRoot2.right)
        else:
            return False


if __name__=='__main__':
    root1 = TreeNode(0)
    root2 = TreeNode(2)
    solution = Solution()
    print(solution.HasSubtree(root1, root2))