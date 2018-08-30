# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 6:
            return index
        t2, t3, t5 = 0, 0, 0
        res = [1]
        for i in range(1,index):
            res.append(min(res[t2]*2,res[t3]*3,res[t5]*5))
            if res[-1] == res[t2]*2:
                t2 = t2+1
            if res[-1] == res[t3]*3:
                t3 += 1
            if res[-1] == res[t5]*5:
                t5 += 1
        return res[-1]


solution = Solution()
print(solution.GetUglyNumber_Solution(7))