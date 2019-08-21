# -*- coding:utf-8 -*-
"""
题目描述
    输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
代码情况：accepted
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    # 写的过程中要注意不要使得链表断开之后找不到下一节点了。
    def Merge(self, pHead1, pHead2):
        # write code here
        # 递归停止条件写法一
        #if not pHead1 and not pHead2:
        #    return None
        #elif not pHead1 and pHead2:
        #    return pHead2
        #elif not pHead2 and pHead1:
        #    return pHead1
        # 写法二，都不用考虑所有情况。但是推荐写法一，更加明确
        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1
        
        if pHead1.val >= pHead2.val:
            pHead2.next = self.Merge(pHead1,pHead2.next)
            return pHead2
        else:
            pHead1.next = self.Merge(pHead1.next,pHead2)
            return pHead1
