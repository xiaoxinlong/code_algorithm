# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        queue = [(pRoot, 1)]
        ans = []
        while queue:
            cur_node, depth = queue.pop(0)
            if len(ans) < depth:
                ans.append([cur_node.val])
            else:
                ans[depth - 1].append(cur_node.val)
            if cur_node.left:
                queue.append((cur_node.left, depth + 1))
            if cur_node.right:
                queue.append((cur_node.right, depth + 1))
        for i in range(1, len(ans)):
            if i % 2 == 1:
                return False
            if ans[i][:len(ans[i] // 2)] != ans[i][len(ans[i]) // 2:]:
                return False
        return True
