# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        left,right = 0,len(array)-1
        while left < right:
            if array[left] + array[right] == tsum:
                return [array[left],array[right]]
            elif array[left] + array[right] < tsum:
                left += 1
            else:
                right -= 1
        return []