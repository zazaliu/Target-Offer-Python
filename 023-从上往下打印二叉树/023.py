# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        """
        :param root:
        :return:
        构建一个队列，每次打印一个节点时，如果该节点有子节点，则把该子节点放入队列的尾部，接下来从队列头部取出一个节点，重复上述过程
        """
        if not root:
            return []
        myStack, res = [], []
        myStack.append(root)
        while myStack:
            node = myStack.pop(0)
            if node.left:
                myStack.append(node.left)
            if node.right:
                myStack.append(node.right)
            res.append(node.val)
        return res