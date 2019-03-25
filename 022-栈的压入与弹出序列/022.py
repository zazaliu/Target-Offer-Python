# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        stack = []
        for pushItem in pushV:
            stack.append(pushItem)
            while stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        for popItem in popV:
            if popItem == stack[-1]:
                stack.pop()
        return not stack