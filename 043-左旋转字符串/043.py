# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        if not s:
            return s
        n = n%(len(s))
        return s[n:]+s[:n]