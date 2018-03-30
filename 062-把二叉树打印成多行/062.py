# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        res = []
        if not pRoot:
            return res
        myStack = []
        myStack.append(pRoot)
        while myStack:
            temp = []
            for i in range(len(myStack)):
                node = myStack.pop(0)
                if node.left:
                    myStack.append(node.left)
                if node.right:
                    myStack.append(node.right)
                temp.append(node.val)
            res.append(temp)
        return res