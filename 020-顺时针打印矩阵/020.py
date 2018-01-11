# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        row, column = len(matrix), len(matrix[0])
        position = 0
        while position < min(column-position, row-position):
            for i in range(position, column-position):
                res.append(matrix[position][i])
            for i in range(position+1,row-position):
                res.append(matrix[i][column-position-1])
            if row-position-1 > position:
                for i in range(column-position-2,position-1,-1):
                    res.append(matrix[row-position-1][i])
            if position < column-position-1:
                for i in range(row-position-2,position,-1):
                    res.append(matrix[i][position])
            position += 1
        return res