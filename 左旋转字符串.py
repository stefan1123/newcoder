# -*- coding: utf-8 -*-

"""
题目描述
    汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指
    令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=
    ”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
代码情况：accepted
"""

class Solution:
    def LeftRotateString(self, s, n):
        # write code here
#        # 方法一： 数组
#        if len(s) <= 0:
#            return ''
#        charlist = list(s)
#        for i in range(n):
#            ch = charlist.pop(0)
#            charlist.append(ch)
#        return ''.join(charlist)
        
        # 方法二：前后两部分分布翻转，再整体翻转。
        if len(s) <= 0:
            return ''
        length = len(s)
        num = n % length
        res = list(s)
        left = res[:num]# 前半部分翻转
        # === 切片操作，会返回新的数组，不会改变原来的数组===
        left = left[::-1]
        right = res[num:]# 后半部分翻转
        right = right[::-1]
        res = left + right # 整体翻转
        res = res[::-1]
        return ''.join(res)
        
        

if __name__ == '__main__':
    sentence = "abcXYZdef"
    print(len(sentence))
    s = Solution()
    ret = s.LeftRotateString(sentence,11) 
    print(len(ret))
