# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        leftDepth = self.TreeDepth(pRoot.left)
        rightDepth = self.TreeDepth(pRoot.right)
        return max(leftDepth,rightDepth)+1