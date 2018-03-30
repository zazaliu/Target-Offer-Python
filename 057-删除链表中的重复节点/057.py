# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        dummy = ListNode(0)
        dummy.next = pHead
        cur = dummy
        flag = False
        while cur.next:
            while cur.next.next and cur.next.next.val == cur.next.val:
                cur.next = cur.next.next
                flag = True
            if flag:
                cur.next = cur.next.next
                flag = False
            else:
                cur = cur.next
        return dummy.next