# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        even = []
        count = 0
        for i in range(len(array)):
            if array[i]%2 == 0:
                even.append(array[i])
            else:
                array[count] = array[i]
                count += 1
        return array[:count]+even