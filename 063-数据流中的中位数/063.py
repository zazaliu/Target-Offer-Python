# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.res = []
        self.mid = None
    def Insert(self, num):
        self.res.append(num)
        self.res.sort()
        length = len(self.res)
        if length%2 == 1:
            self.mid = self.res[(length-1)/2]
        else:
            self.mid = (self.res[length/2]+self.res[(length/2)-1])/2.0
    def GetMedian(self,ok):
        return self.mid