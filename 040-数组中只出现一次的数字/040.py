# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        res = []
        for i in array:
            if i not in res:
                res.append(i)
            else:
                res.remove(i)
        return res