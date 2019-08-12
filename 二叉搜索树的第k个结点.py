"""
题目描述
    给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，
    按结点数值大小顺序第三小结点的值为4。
代码情况：accepted
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # 返回对应节点TreeNode
#    def KthNode(self, pRoot, k):
#        # write code here
#        # 二叉树中序遍历
#        if k<1 or not pRoot:
#            return None
#        nodelist = []
#        
#        def inorder(root):
#            if not root:
#                return
#            inorder(root.left)
#            nodelist.append(root)
#            inorder(root.right)
#        inorder(pRoot)
#        if k > len(nodelist):
#            return None
#        return nodelist[k-1]
    
    def __init__(self):
        self.res = []
        
    def KthNode(self, pRoot, k):
        # write code here
        # 二叉树中序遍历
        if k<1 or not pRoot:
            return None
        self.inorder(pRoot)
        if k > len(self.res):
            return None
        return self.res[k-1]
        
    def inorder(self,root):
        if not root:
            return None
        self.inorder(root.left)
        self.res.append(root)
        self.inorder(root.right)
