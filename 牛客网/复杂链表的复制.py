# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead==None:
            return None
        # step 1
        head = pHead
        while head:
            headnext = head.next
            temp = RandomListNode(head.label)
            temp.next = headnext
            head.next = temp
            head = headnext

        # step 2
        head = pHead
        while head:
            temp = head.next
            if head.random!=None:
                temp.random = head.random.next
            head = temp.next
        # step 3
        dummy = pHead
        res = pHead.next
        while dummy:
            new_head = dummy.next
            dummynext = new_head.next
            dummy.next = dummynext
            if dummynext:
                new_head.next = dummynext.next
            else:
                new_head.next = None
            dummy = dummynext

        return res
if __name__=='__main__':
    L = [1,2,3,4,5]
    Node = [RandomListNode(i) for i in L]
    for i in range(4):
        Node[i].next = Node[i+1]
    Node[2].random = Node[1]
    s = Solution()
    sc = s.Clone(Node[0])
    print("ss")



