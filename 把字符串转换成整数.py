# -*- coding:utf-8 -*-
"""
题目描述
  将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 
  数值为0或者字符串不是一个合法的数值则返回0。
输入描述:
  输入一个字符串,包括数字字母符号,可以为空
输出描述:
  如果是合法的数值表达则返回该数字，否则返回0
示例1
  输入
    +2147483647
        1a33
  输出
    2147483647
        0
代码情况：accepted
"""
class Solution:
    def StrToInt(self, s):
        # write code here
        # 排除非法输入（即异常情况）
        if s in ['','-','+','-+','+-']:
            return 0
        errCharCnt = 0
        # 当含有不属于'012345678-+'范围内的字符(即非法字符)，errCharCnt加1
        for c in s:
            if c not in '0123456789-+':
                errCharCnt += 1
        # 只要-+号不在第一位就非法
        for c in s[1:]:
            if c not in '0123456789':
                errCharCnt += 1                
        # 含有非法字符        
        if errCharCnt:
            return 0
        return int(s)

if __name__ == '__main__':
    c = '4-123'
    res = Solution().StrToInt(c)
