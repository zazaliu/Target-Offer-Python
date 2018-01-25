# -*- coding:utf-8 -*-
class Solution:
    def Print1ToMaxN(self, n):
        # write code here
        """
        :param n:
        :return:
        python中long数据类型理论上可以存放无限大整数，因而不存在大数问题
        （python2中当整数过大时，会自动转换为long，因而也不存在大数问题）
        """
        res = [0, 1, 1]
        if n <= 2:
            return res[n]
        for i in range(3, n+1):
            res.append(res[i-2]+res[i-1])
        return res[n]