# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        def treeDepth(root):
            if not root:
                return 0
            left = treeDepth(root.left)
            right = treeDepth(root.right)
            return max(left,right)+1
        if not pRoot:
            return True
        leftDepth = treeDepth(pRoot.left)
        rightDepth = treeDepth(pRoot.right)
        if abs(leftDepth-rightDepth) <= 1:
            return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
        else:return False