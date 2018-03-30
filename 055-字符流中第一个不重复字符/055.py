# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.res = ''
    def FirstAppearingOnce(self):
        onlyList = list(self.res)
        for i in onlyList:
            if onlyList.count(i) == 1:
                return i
        return '#'
    def Insert(self, char):
        self.res += char