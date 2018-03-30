# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        def subTree(l,r):
            if not l and not r:
                return True
            if l and r and l.val == r.val:
                return subTree(l.left,r.right) and subTree(l.right,r.left)
            return False
        if pRoot:
            return subTree(pRoot.left,pRoot.right)
        return True