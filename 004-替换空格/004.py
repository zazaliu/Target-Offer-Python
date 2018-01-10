class Solution:
    def replaceSpace(self, s):
        return s.replace(' ', '%20')


S1 = Solution()
s = 'We are happy'
print(S1.replaceSpace(s))