"""
题目描述
    牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish
    写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后
    来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。Cat对
    一一的翻转这些单词顺序可不在行，你能帮助他么？
代码情况：方法一：acc; 方法二：bug
"""

class Solution:
    def ReverseSentence(self, s):
        # write code here
#        # 方法一：借助python的特性，太过于简单了
#        if len(s)<=0:
#            return ''
#        res = s.split(' ')
#        return ' '.join(res[::-1])       
        
        # 方法二：设计一个可以反转字符串的函数，有bug
        if len(s)<=0:
            return ''

        res = self.reverse(s,0,len(s)-1)
        
        
        left = 0
        right = 0
        maxIndex = len(res)-1
        
        while right<=maxIndex:
            if res[right]!= ' ':
                right += 1
            else:
                res[left:right+1] = self.reverse(res,left,right)
                left = right+1
                right += 1
                
        res = ''.join(res)
        return res
        
    def reverse(self,arr,start,end):
        newarr = []
        while start<=end:
            newarr.append(arr[end])
            end -= 1
        return newarr
