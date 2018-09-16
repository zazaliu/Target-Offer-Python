# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        res = []
        for i in array:
            if i not in res:
                res.append(i)
            else:
                res.remove(i)
        return res
    
    def FindNumsAppearOnce1(self, array):
        # write code here
        """
        此题用了两次异或运算特点：
        （1）第一次使用异或运算，得到了两个只出现一次的数相异或的结果。
        （2）因为两个只出现一次的数肯定不同，即他们的异或结果一定不为0，
        一定有一个位上有1。另外一个此位上没有1，我们可以根据此位上是否
        有1，将整个数组重新划分成两部分，一部分此位上一定有1，另一部分
        此位上一定没有1，然后分别对每部分求异或，因为划分后的两部分有
        这样的特点：其他数都出现两次，只有一个数只出现一次。因此，我们
        又可以运用异或运算，分别得到两部分只出现一次的数。
        """
        if not array:
            return []
        xor = 0
        for i in array:
            xor = xor ^ i
        position = 0
        while (xor & 1) == 0:
            xor = xor >> 1
            position += 1
        x1, x2 = 0, 0
        for i in array:
            if (i >> position) & 1:
                x1 = x1 ^ i
            else:
                x2 = x2 ^ i
        return [x1, x2]