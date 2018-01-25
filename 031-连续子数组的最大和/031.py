# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        res = [0 for i in array]
        res[0] = array[0]
        for i in range(1,len(array)):
            if res[i-1] > 0:
                res[i] = res[i-1]+array[i]
            else:
                res[i] = array[i]
        return max(res)