"""
题目描述
    请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的
    顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
代码情况：accepted
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def Print(self, pRoot):
        # write code here
"""
解法：简单画个图看看，就可以知道，奇数层是从左往右打印，偶数层是从右往左打印。
    当不走之字形路线时，可以使用队列逐层访问，并同时保存孩子节点（先左后右）；
    需要走之字形只有偶数层不太一样，设置flag，到偶数层就把访问到的节点的数字导一下序即可
"""
        if not pRoot:
            return []
        # 用队列保存即将要访问的每一层节点
        level = [pRoot]
        res = []
        # 对于偶数层需要从右往左
        right2left = False
        while level:
            curvals = []
            curlevel = []
            for node in level:
                curvals.append(node.val)
                if node.left:
                    curlevel.append(node.left)
                if node.right:
                    curlevel.append(node.right)
            if right2left:
                curvals = curvals[::-1]
            res.append(curvals)
            level = curlevel
            # 下一层的flag需要取反
            right2left = not right2left
        return res
