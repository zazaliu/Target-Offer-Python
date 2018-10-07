# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss) == 1:
            return [ss]
        res = []
        for i in range(len(ss)):
            temp = self.Permutation(ss[:i]+ss[i+1:])
            for j in temp:
                res.append(ss[i]+j)
        return sorted(list(set(res)))