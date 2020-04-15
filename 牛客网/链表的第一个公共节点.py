# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val)
class Solution:
    @classmethod
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1==pHead2:
            return pHead1
        elif not pHead1 or not pHead2:
            return None
        s1 = pHead1
        s2 = pHead2
        while s1 and s2:
            s1 = s1.next
            s2 = s2.next
            if s1==s2:
                return s1
        if s1==None:
            s1 = pHead2
            while s1 and s2:
                s1 = s1.next
                s2 = s2.next
            s2 = pHead1
            while s1 and s2:
                s1 = s1.next
                s2 = s2.next
                if s1==s2:
                    return s1
            return None
        else:
            s2 = pHead1
            while s1 and s2:
                s1 = s1.next
                s2 = s2.next
            s1 = pHead2
            while s1 and s2:
                s1 = s1.next
                s2 = s2.next
                if s1==s2:
                    return s1
            return None

if __name__=="__main__":
    l1 = ListNode(0)
    l1.next = ListNode(3)
    l1.next.next = ListNode(5)
    l2 = ListNode(2)
    l2.next = ListNode(8)
    print(l1)
    print(Solution.FindFirstCommonNode(l1,l2))