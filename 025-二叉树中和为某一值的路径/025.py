# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        res = []
        if not root:
            return []
        self.FindWay(root,[],expectNumber,res)
        return res
    def FindWay(self,root,path,cur,res):
        cur -= root.val
        p = path[:]
        p.append(root.val)
        if root.left:
            self.FindWay(root.left,p,cur,res)
        if root.right:
            self.FindWay(root.right,p,cur,res)
        if not root.left and not root.right:
            if cur == 0:
                res.append(p)