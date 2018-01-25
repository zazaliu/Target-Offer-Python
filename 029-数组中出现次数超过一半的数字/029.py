# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return None
        value, count = numbers[0], 1
        for i in range(1,len(numbers)):
            if count == 0:
                value, count = numbers[i], 1
            elif numbers[i] == value:
                count += 1
            else:
                count -= 1
        return value if numbers.count(value) > len(numbers)/2 else 0