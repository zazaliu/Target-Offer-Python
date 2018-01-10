# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k == 0:
            return None
        fast = slow = head
        for i in range(k-1):
            if fast and fast.next:
                fast = fast.next
            else:
                return None
        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow