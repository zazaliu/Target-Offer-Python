
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        head,tail = [1],[1]
        for i in range(len(A)-1):
            head.append(A[i]*head[i])
            tail.append(A[-i-1]*tail[i])
        return [head[i]*tail[-i-1] for i in range(len(A))]