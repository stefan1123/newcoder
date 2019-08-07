"""
题目描述
    输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
代码情况：accepted
"""
class Solution:
#    def TreeDepth(self, pRoot):
#        # write code here
#        # 方法一：深度优先遍历
#        if pRoot == None:
#            return 0
#        res = [] # 保存所有路径
#        onepath = [] # 保存单挑路径
#        self.Find(pRoot,res,onepath)
#        maxlen = 0
#        for l in res:
#            if len(l)>maxlen:
#                maxlen = len(l)
#        return maxlen
#             
#    def Find(self,root,res,path):
#        if root == None:
#            return
#        # 保存当前非空节点在一条路径中
#        path.append(root)
#        # 判断该结点是否是叶子节点
#        isleaf = (not root.left) and (not root.right)
#        # 若是叶子节点，则把该路径放入res中
#        if isleaf:
#            ### !!!!!!!!!note!!!!!!!!!
#            # 必须使用path[:]切片复制path数组，否则添加不进res数组中
#            # res.append(path) # error
#            res.append(path[:])
#        if root.left:
#            self.Find(root.left,res,path)
#        if root.right:
#            self.Find(root.right,res,path)
#        # 从单路径回到父节点路径
#        path.pop()
    
    def TreeDepth(self, pRoot):
        # 方法二：树的深度等于左子树与右子树最大深度加1
        # 空结点时，深度为0
        if pRoot == None:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        
        return left+1 if left > right else right+1
