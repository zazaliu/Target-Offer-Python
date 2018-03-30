# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if k <= 0:
            return None
        res = []
        self.InOrderTraverse(pRoot,k,res)
        return res[k-1] if k <= len(res) else None
    def InOrderTraverse(self, root, k, res):
        if not root:
            return
        self.InOrderTraverse(root.left, k, res)
        res.append(root)
        self.InOrderTraverse(root.right, k, res)