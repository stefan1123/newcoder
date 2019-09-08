# -*- coding:utf-8 -*-
"""
题目描述
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
代码情况：accepted
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        result = []
        onepath = []
        self.Find(root,result,onepath,expectNumber)
        return result
        
    def Find(self,root,res,path,expectnum):
        if root is None:
            return
        # 先把该节点的值加到路径列表中
        path.append(root.val)
        # 判断是否是叶子节点
        isleaf = (not root.left) and (not root.right)
        # 当已经是叶子节点且值相等，则将该path加入到返回列表res中
        if isleaf and expectnum == root.val:
            res.append(path[:]) # 必须使用path[:],path报错

        # 如果不是叶子节点，则继续递归向下，访问至叶子节点
        if root.left:
            self.Find(root.left,res,path,expectnum-root.val)
        if root.right:
            self.Find(root.right,res,path,expectnum-root.val)
        # 如果该节点访问后依旧没获得expectnum，则在path中将最后一个值弹出，使得path中回到叶子节点的父节点
        path.pop()
