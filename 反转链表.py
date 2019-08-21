# -*- coding:utf-8 -*-
"""
题目描述
  输入一个链表，反转链表后，输出新链表的表头。
代码情况： accpeted
"""
"""
解法：
  假设有链表： a-->b-->c-->d-->e
  现在c的前几个已经反转，即链表现在的情况为 a<--  b  <-- c      d  -->e , 需要反转节点c(即，改变c的next指针指向)。
                                             prev   pnode  pnext
  考虑一种情况，要是直接把c的next指向b，可能会丢失节点d. 所以，需要设置三个指针，分别指向当前遍历到的节点、它的前一个节点以及后一个节点。
  另外，反转后的链表的头节点是原始链表的尾节点。什么结点是尾节点？自然是next为None的节点。即，当当前节点的next为空，此时将该节点赋值给
  初始化时定义的新链表头节点。
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None:
            return None
        pnew = pHead
        pnode = pHead
        prev = None
        while pnode:
            pnext = pnode.next
            if pnext == None:
                pnew = pnode
            pnode.next = prev
            prev = pnode
            pnode = pnext
        return pnew
