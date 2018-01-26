# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        """
        :param array:
        :return:
        动态规划：找出递推关系式：
        用函数f(i)表示咦i个数字结尾的子数组的最大和，则：
        if i == 0 or f(i-1) < 0:
            f(i) = array[i]
        elif i != 0 and f(i-1) > 0:
            f(i) = f(i-1)+array[i]
        则f(x)的最大值即为该数组的连续子数组的最大和
        """
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