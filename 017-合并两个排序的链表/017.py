# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        dummy = ListNode(0)
        step = dummy
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                temp = ListNode(pHead1.val)
                pHead1 = pHead1.next
            else:
                temp = ListNode(pHead2.val)
                pHead2 = pHead2.next
            step.next = temp
            step = step.next
        if pHead1:
            step.next = pHead1
        elif pHead2:
            step.next = pHead2
        return dummy.next