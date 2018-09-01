# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        if not root:
            return ['#']
        return [root.val] + self.Serialize(root.left) + self.Serialize(root.right)
    def Deserialize(self, s):
        return self.De(s)
    def De(self,s):
        temp = s.pop(0)
        if temp != '#':
            root = TreeNode(temp)
            root.left = self.De(s)
            root.right = self.De(s)
        else: root =None
        return root