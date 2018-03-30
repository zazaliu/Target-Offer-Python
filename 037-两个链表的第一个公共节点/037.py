# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        pLength1, pLength2 = 0, 0
        p1, p2 = pHead1, pHead2
        while pHead1:
            pLength1 += 1
            pHead1 = pHead1.next
        while pHead2:
            pLength2 += 1
            pHead2 = pHead2.next
        if pLength2 > pLength1:
            for i in range(pLength2 - pLength1):
                p2 = p2.next
        else:
            for i in range(pLength1 - pLength2):
                p1 = p1.next
        while p1 != p2:
            p1, p2 = p1.next, p2.next
        return p1
