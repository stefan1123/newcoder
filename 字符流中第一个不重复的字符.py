"""
题目描述
    请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个
    只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
代码情况：accepted

"""

class Solution:
    def __init__(self):
        self.word = []
    # 返回对应char
    """
    第一次遇到数据流的题目，记录数据流应该使用队列，具体到python中即使用list;
    该题解法是可以使用hasamap,只不过要使用两次，一次统计字符出现的次数，一次用于找出只出现一次
    的第一个字符。时间复杂度O(N)，空间复杂度O(N)
    """
    def FirstAppearingOnce(self):
        # write code here
        hashmap = {}
        for ch in self.word:
            if ch not in hashmap.keys():
                hashmap[ch] = 0
            hashmap[ch] += 1
        
        for ch in self.word:
            if hashmap[ch] == 1:
                return ch
        return '#'
                
    def Insert(self, char):
        # write code here
        self.word.append(char)
