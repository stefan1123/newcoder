"""
题目描述(acc)
输入两个链表，找出它们的第一个公共结点。
"""
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here 
#        # 方法一： 使用hashmap的思想，把链表1的节点放入list,再遍历链表2，看是否含有相同节点
#        if pHead1 == None or pHead2 ==None:
#            return None
#        nodelist = []
#        p = pHead1
#        while p:
#            nodelist.append(p)
#            p = p.next
#        p = pHead2
#        while p:
#            if p in nodelist:
#                return p
#            p = p.next
#        return None
        
        # 方法二：先遍历链表，找出最长的链表，如果有公共节点，则两链表应该有相同的一部分尾巴。
        # 假设链表1长n,链表2长m(n>m),则先让链表1走（n-m）次，然后两个链表一起走，再判断是否走到相同节点。
        if pHead1 == None or pHead2 ==None:
            return None
        n = 0
        m = 0
        p = pHead1
        while p:
            n += 1
            p = p.next
        p = pHead2
        while p:
            m += 1
            p = p.next
        if n>m:
            h1 = pHead1
            h2 = pHead2
            delt = n-m
            while delt and h1:
                h1 = h1.next
                delt -= 1
            while h1 and h2:
                if h1 == h2:
                    return h1
                else:
                    h1 = h1.next
                    h2 = h2.next
            return None
            
        else:
            h1 = pHead1
            h2 = pHead2
            delt = n-m
            while delt and h2:
                h2 = h2.next
                delt -= 1
            while h1 and h2:
                if h1 == h2:
                    return h1
                else:
                    h1 = h1.next
                    h2 = h2.next
            return None
