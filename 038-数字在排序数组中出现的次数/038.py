# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        if k not in data:
            return 0
        count = 0
        left,right = 0,len(data)-1
        while left <= right:
            mid = (left+right)/2
            if data[mid] < k:
                left = mid+1
            elif data[mid] > k:
                right = mid-1
            else:break
        i,j = mid,mid
        while i >= 0:
            if data[i] == k:
                count += 1
            else:break
            i -= 1
        while j <= len(data)-1:
            if data[j] == k:
                count += 1
            else:break
            j += 1
        return count-1