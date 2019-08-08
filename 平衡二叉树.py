# -*- coding: utf-8 -*-
"""
题目描述
  输入一棵二叉树，判断该二叉树是否是平衡二叉树。
代码情况：accepted
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
#    def IsBalanced_Solution(self, pRoot):
#        # write code here
#        # 方法一: 判断某一节点上的左右子树的平衡因子。按此法逐个判断节点。
#        # 缺点：很多节点重复访问，速度慢
#        if pRoot == None:
#            return True
#        left = self.treeDepth(pRoot.left)
#        right = self.treeDepth(pRoot.right)
#        diff = left - right
#        
#        if diff>1 or diff<-1: 
#            return False
#        # 按照AVL的定义，递归判断左右子树是否是平衡二叉树
#        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
#    
#    def treeDepth(self,root):
#        # 类似深度优先遍历
#        if root == None:
#            return 0
#        left = self.treeDepth(root.left)
#        right = self.treeDepth(root.right)
#        
#        return left+1 if left>right else right+1
        
    # 方法二：后序遍历，每个节点只访问一次，只有某节点的左右子树为平衡树，才能继续判断该节点的父节点    
    def IsBalanced_Solution(self, pRoot):
        bool_flag,depth = self.IsAVL(pRoot)
        return bool_flag
        
    def IsAVL(self,root):
        # 空树也是平衡二叉树，深度为0
        if root == None:            
            return True, 0
        # flag,depth, 判断左右子树是否为AVL
        flag_l, depth_l = self.IsAVL(root.left)
        flag_r, depth_r = self.IsAVL(root.right)
        
        if flag_l and flag_r:
            diff = depth_l - depth_r
            if diff<=1 and diff>=-1:
                d = 1+max(depth_l,depth_r)
                return True, d
        return False, 0
        

    
    
        
        
