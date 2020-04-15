# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root.val > expectNumber:
            return None
        elif root.val == expectNumber:
            if root.left != None and root.right != None:
                return None
            elif root.left == None or root.right == None:
                return [[root.val]]
        elif root.val < expectNumber:
            ans = []
            if root.left:
                t1 = self.FindPath(root.left, expectNumber - root.val)
                if t1:
                    ans.extend([[root.val] + t for t in t1])
            if root.right:
                t2 = self.FindPath(root.right, expectNumber - root.val)
                if t2:
                    ans.extend([[root.val] + t for t in t2])
            if len(ans) > 0:
                return ans
            else:
                return None
