# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        res = [0, 1, 1]
        if n <= 2:
            return res[n]
        for i in range(3, n+1):
            res.append(res[i-2]+res[i-1])
        return res[n]