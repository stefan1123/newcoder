"""
题目描述
  输入一个链表，输出该链表中倒数第k个结点。
"""
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if (not head)or (k==0):
            return None
        pfast = head
        plow = head
        # 由于初始化的指针指向第一个节点，所以指针只需要再向后移动k-1次
        for i in range(k-1):
            if pfast.next:
                pfast = pfast.next
            # 若是链表长度小于 k ，返回 None
            else:
                return None
        while pfast.next:
            plow = plow.next
            pfast = pfast.next
        return plow
