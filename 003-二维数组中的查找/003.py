# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if array == [] or array == [[]]:
            return False
        depth, width = len(array), len(array[0])
        row, column = 0, width-1
        while column >= 0 and row <= depth-1:
            if array[row][column] == target:
                return True
            elif array[row][column] > target:
                column = column-1
            elif array[row][column] < target:
                row = row+1
        return False