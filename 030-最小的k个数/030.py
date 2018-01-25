# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput) or k == 0:
            return []
        res = tinput[:k]
        res.sort()
        for i in range(k,len(tinput)):
            if tinput[i] < res[-1]:
                res[-1] = tinput[i]
                res.sort()
        return res