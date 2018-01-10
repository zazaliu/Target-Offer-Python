# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        left, right = 0, len(rotateArray)-1
        while left < right:
            mid = left+(right-left)/2
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            else:
                right = mid
            if left+1 == right:
                return min(rotateArray[left],rotateArray[right])
        return rotateArray[left]