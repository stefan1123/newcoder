"""
题目描述
    给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中
    的结点不仅包含左右子结点，同时包含指向父结点的指针。
代码情况：accepted

"""

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode == None:
            return None
        # 若右子树存在，找右孩子为根结点的子树的最左边的节点
        if pNode.right:
            root_rightTree = pNode.right
            if root_rightTree.left:
                node = root_rightTree.left
                while node.left:
                    node = node.left
                return node
            else:
                return root_rightTree    
        # 右子树不存在    
        else:            
            # 若该节点是其父亲节点的左节点，则下一节点就是其父节点
            if pNode.next and  pNode == pNode.next.left:
                return pNode.next
            # 若该节点不是其父亲节点的左节点，则，网上遍历父节点，找到某一个节点M，使这个
            # 节点M的父节点N的左节点正好是该节点,测试父节点N就是下一节点
            else:
                while pNode.next and pNode != pNode.next.left:
                    pNode = pNode.next
                return pNode.next
             
             # 简洁一点的
#            # 若该节点是其父亲节点的左节点，则下一节点就是其父节点
#            # 若该节点不是其父亲节点的左节点，则，向上遍历父节点，找到某一个节点M，使这个
#            # 节点M的父节点N的左节点正好是该节点,此时父节点N就是下一节点
#            while pNode.next:
#                tmp=pNode.next
#                if tmp.left==pNode:
#                    return tmp
#                pNode=tmp
                
                
