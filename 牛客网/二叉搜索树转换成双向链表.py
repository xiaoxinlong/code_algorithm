class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree == None:
            return pRootOfTree
        new_head, new_tail = self.Convert2Node(pRootOfTree)
        return new_head

    def Convert2Node(self, root):

        if root.left:
            left_head, left_tail = self.Convert2Node(root.left)
            root.left = left_tail
            left_tail.right = root
        else:
            left_head = root
        if root.right:
            right_head, right_tail = self.Convert2Node(root.right)
            root.right = right_head
            right_head.left = root
        else:
            right_tail = root

        return left_head, right_tail