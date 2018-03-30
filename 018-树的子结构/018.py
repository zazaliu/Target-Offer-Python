# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        res = False
        if pRoot1.val == pRoot2.val:
            res = self.check(pRoot1,pRoot2)
        if not res:
            return self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)
        else:
            return True
    def check(self,p1,p2):
        if not p2:
            return True
        elif not p1:
            return False
        if p1.val == p2.val:
            return self.check(p1.left,p2.left) and self.check(p1.right,p2.right)
        else:
            return False