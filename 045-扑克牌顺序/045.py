# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        minValue,maxValue = 14,0
        res = []
        for i in numbers:
            if i != 0:
                minValue,maxValue = min(i,minValue),max(i,maxValue)
                res.append(i)
        if maxValue - minValue <= 4 and len(res) == len(list(set(res))) and numbers:
            return True
        return False