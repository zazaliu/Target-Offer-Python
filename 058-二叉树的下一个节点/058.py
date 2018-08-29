# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):      # 先中序遍历得到遍历结果，然后查找需要节点的下一个节点即可
        root = pNode
        while root.next:
            root = root.next
        self.res = []
        self.Inorder(root)
        temp = self.res.index(pNode)
        if temp < len(self.res)-1:
            return self.res[temp+1]
    def Inorder(self,pNode):
        if not pNode:
            return
        self.Inorder(pNode.left)
        self.res.append(pNode)
        self.Inorder(pNode.right)




    def GetNext1(self, pNode):
        if not pNode:
            return None
        # 第一种情况：给定节点有右节点
        # 返回给定节点右子树的最左节点
        if pNode.right:
            temp = pNode.right
            while temp.left:
                temp = temp.left
            return temp
        # 第二种情况：给定节点没有右节点，根据起父节点的值判断
        # 2.1情况：如果父节点的左节点为给定节点，则返回父节点
        while pNode.next:
            temp = pNode.next
            if temp.left == pNode:
                return temp
            # 2.1情况：向上回溯，找到满足父节点的左节点为给定节点
            pNode = pNode.next
        return None