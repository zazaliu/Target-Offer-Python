# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        product = 1
        if exponent == 0:
            return product
        flag = True if exponent > 0 else False
        exponent = abs(exponent)
        temp = base
        while exponent > 1:
            if exponent%2 == 1:
                product *= temp
            base = base*base
            exponent = exponent/2
            temp = base
        return product*base if flag == True else 1/(product*base)