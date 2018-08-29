# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        if not size or size > len(num):
            return []
        res = []
        maxValue = max(num[:size])
        res.append(maxValue)
        for i in range(0,len(num)-size):
            if num[i] == maxValue:
                maxValue = max(num[i+1:i+size+1])
            elif num[i+size] > maxValue:
                maxValue = num[i+size]
            res.append(maxValue)
        return res