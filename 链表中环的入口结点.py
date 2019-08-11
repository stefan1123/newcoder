"""
题目描述
    给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
代码情况：accepted
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        # 1)先找获得环的长度n;
        #  1.1 设置一快一慢指针，快指针一次走两步，慢指针一次走一步；
        #  1.2 如果快指针走到None了，说明没环；否则，有环就会相遇；
        #  1.3 相遇节点处，设count=1，其中一个指针再走一圈（减1），count记录走过的节点数，该指针
        #       的next与相遇点相等时，count就为环的节点数
        # 2)从新设置两个指针指向头结点，其中一个先走count步，然后两指针同时走（一次一步），相遇时该节点
        #       就是环的入口节点
        if pHead == None:
            return None
        meetingNode = self.meetNode(pHead)
        if meetingNode == None:
            return None
        p = meetingNode        
        cnt = 1 # 环中的节点数n
        while p.next != meetingNode:
            p = p.next
            cnt+=1
        # 设置新的两个指针，其中一个先走n步，然后两指针再一块走，相遇的节点就是环的入口节点
        p = pHead
        q = pHead
        for i in range(cnt):
            p = p.next
        while p!=q:
            p=p.next
            q=q.next
        return p
                
    def meetNode(self,root):
        # 设置两指针，一个一次走一步，一个一次走两步,找到相遇的节点
        # 慢指针起点
        pslow = root.next
        if pslow == None:
            return None
        # 快指针起点
        pfast = pslow.next
        # 快慢指针都存在时（即快指针还没到链表尾None）
        while pslow and pfast:
            # 如果相等，就是遇上了，最小的环三个节点就行            
            if pslow == pfast:
                return pslow
            # 否则，慢指针走一步
            pslow = pslow.next
            # 快指针先走一步，然后查看其是否走到尾部
            # 如果没有，说明有环存在，如果没环一定会走到None的位置
            pfast = pfast.next            
            if pfast.next:
                pfast = pfast.next
            else:
                return None # 没环
