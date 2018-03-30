# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        fast,slow = pHead,pHead
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        slow = pHead
        while fast != slow:
            fast,slow = fast.next,slow.next
        return fast

    def EntryNodeOfLoop1(self, pHead):
        res = []
        p = pHead
        while p:
            if p in res:
                return p
            else:
                res.append(p)
                p = p.next