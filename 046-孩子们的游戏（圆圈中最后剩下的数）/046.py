# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n <= 0:
            return -1
        res = [0]
        for i in range(1,n):
            temp = (res[-1]+m)%(i+1)
            res.append(temp)
        return res[-1]

    def LastRemaining_Solution1(self, n, m):
        if n <= 0:
            return -1
        memberList = [i for i in range(n)]
        start, target = 0, -1
        while memberList:
            kTarget = (start + m - 1) % len(memberList)
            target = memberList.pop(kTarget)
            start = kTarget
        return target