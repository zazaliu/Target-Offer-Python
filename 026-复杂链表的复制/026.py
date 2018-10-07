# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead: return
        newNode = RandomListNode(pHead.label)
        newNode.random = pHead.random
        newNode.next = self.Clone(pHead.next)
        return newNode