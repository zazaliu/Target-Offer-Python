# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        matrix = [[0 for i in range(cols)] for j in range(rows)]
        def checkSum(row,col):
            res = 0
            for i in str(row):
                res += int(i)
            for j in str(col):
                res += int(j)
            return res <= threshold
        def check(row,col):
            if 0 <= row < rows and 0 <= col < cols and checkSum(row,col) and matrix[row][col] == 0:
                matrix[row][col] = 1
                return check(row-1,col)+check(row,col-1)+check(row+1,col)+check(row,col+1)+1
            else:return 0
        result = check(0,0)
        return result

s= Solution()
print(s.movingCount(5,10,10))