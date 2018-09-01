# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        res = []
        if not pRoot:
            return res
        myStack = []
        myStack.append(pRoot)
        flag = True
        while myStack:
            temp = []
            for i in range(len(myStack)):
                node = myStack.pop(0)
                if node.left:
                    myStack.append(node.left)
                if node.right:
                    myStack.append(node.right)
                temp.append(node.val)
            if flag:
                res.append(temp)
            else:res.append(temp[::-1])
            flag = not flag
        return res