"""
题目描述
    在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 
    例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
代码情况：accepted

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        # 建立新的链表和一个指针记录当前新链表中不重复的最后一个节点
        first = ListNode(-1)     # 为了避免重复，在链表开始之前新建一个头结点。
        first.next = pHead
        curr = pHead   # 作为遍历链表的指针
        pre = first    # 记录不重复节点之前的最后信息，pre连接的节点就是新的链表的最后结果
        while curr and curr.next:
            if curr.val != curr.next.val:  # 当前节点不重复，继续往下走
                curr = curr.next
                pre = pre.next
            else:      # 如果重复，找到不重复节点为止。
                val = curr.val
                while curr and curr.val == val:
                    curr = curr.next
                pre.next = curr  
                # 这里直接令pre.next等于第一个与当前元素不重复的节点即可，
                # 不用管这个节点也是重复节点，因为pre一定不重复，且被固定了下来，
                # 是不变的，如果这个节点也是重复节点，pre.next会再次更新。
        return first.next
