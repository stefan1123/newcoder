"""
题目描述
    请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此
    二叉树的镜像是同样的，定义其为对称的。
代码情况：accepted

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        # 通常使用的遍历方法有：前序遍历，中序遍历，后续遍历，三种方法都是先遍历左节点，再遍历右节点。
        # 考虑一种情况，无论使用前中后哪种遍历方式，设计一种对称的遍历算法，先遍历右节点再遍历左节点。
        # 以前序遍历为例：正常的是，父节点-->左节点-->右节点，
        #               对称的是，父节点-->右节点-->左节点。
        if not pRoot:
            return True
        return self.isSameNode(pRoot,pRoot)
    
    def isSameNode(self,root1,root2):
        # 当节点有空时，只有两个同时为None才为True,否则任意一个非空，另一个为空则为False
        # if not root1 and not root2：## 注意标点符号，又被坑了！！！
        if not root1 and not root2:
            return True
        if root1 and not root2:
            return False
        if not root1 and root2: 
            return False
        # 当节点均非空时,只要值不等则False,否则递归对比下一节点
        if (root1.val) != (root2.val):
            return False
        # 采用熔断算法
        left = self.isSameNode(root1.left,root2.right)
        if not left:
            return False
        right = self.isSameNode(root1.right, root2.left)
        if not right:
            return False
        return True
