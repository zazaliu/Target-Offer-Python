# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        sList = s.split(' ')
        sList = sList[::-1]
        return ' '.join(sList)