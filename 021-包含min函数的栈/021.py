# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.res = []
        self.minValue = 10000000
    def push(self, node):
        self.res.append(node)
        self.minValue = min(self.minValue,node)
    def pop(self):
        self.minValue = min(self.res[:len(self.res)-1])
        return self.res.pop()
    def top(self):
        self.minValue = min(self.res[1:])
        return self.res.pop(0)
    def min(self):
        return self.minValue