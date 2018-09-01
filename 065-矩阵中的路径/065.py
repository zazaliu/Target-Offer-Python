# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j] == path[0]:
                    if self.findPath(list(matrix), rows, cols, i, j, path[1:]):
                        return True
    def findPath(self, matrix, rows, cols, i, j, path):
        if not path:
            return True
        matrix[i*cols+j] = '#'
        if j+1 < cols and matrix[i*cols+j+1] == path[0]:
            return self.findPath(matrix, rows, cols, i, j+1, path[1:])
        elif j-1 >= 0 and matrix[i*cols+j-1] == path[0]:
            return self.findPath(matrix, rows, cols, i, j-1, path[1:])
        elif i+1 < rows and matrix[(i+1)*cols+j] == path[0]:
            return self.findPath(matrix, rows, cols, i+1, j, path[1:])
        elif i-1 >= 0 and matrix[(i-1)*cols+j] == path[0]:
            return self.findPath(matrix, rows, cols, i-1, j, path[1:])
        else:
            return False