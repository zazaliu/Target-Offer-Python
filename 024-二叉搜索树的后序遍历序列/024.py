# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        mid = len(sequence)-1
        for i in range(len(sequence)):
            if sequence[i] > sequence[-1]:
                mid = i
                print(mid)
                break
        for i in range(mid,len(sequence)):
            if sequence[i] < sequence[-1]:
                return False
        left, right = True, True
        if mid > 0:
            left = self.VerifySquenceOfBST(sequence[:mid])
        if mid < len(sequence)-1:
            right = self.VerifySquenceOfBST(sequence[mid:len(sequence)-1])
        return left and right



solution = Solution()
print(solution.VerifySquenceOfBST([6,7]))