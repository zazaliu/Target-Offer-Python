# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ''
        def cmp(s1,s2):
            if int(str(s1)+str(s2)) > int(str(s2)+str(s1)):
                return 1
            else:
                return -1
        numbers = sorted(numbers,cmp)
        res = ''
        for i in numbers:
            res += str(i)
        return int(res)