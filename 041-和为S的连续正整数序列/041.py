# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        res = []
        for i in range(tsum,1,-1):
            if i % 2 == 1 and tsum % i == 0:
                pro = tsum/i
                ran = (i-1)/2
                temp = [i for i in range(pro-ran,pro+ran+1)]
                if temp[0] > 0 and temp not in res:
                    res.append(temp)
            if i % 2 == 0 and ((tsum/i)*i + i/2) == tsum:
                pro = tsum/i
                ran = i/2
                temp = [i for i in range(pro-ran+1,pro+ran+1)]
                if temp[0] > 0 and temp not in res:
                    res.append(temp)
        return res