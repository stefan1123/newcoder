"""
题目描述
    请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123",
    "3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
代码情况：accepted

"""

# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
"""
数字的格式可以用A[.[B]][E|eC]或者.B[E|eC]表示，其中A和C都是整数（可以有符号也可以没有），B是一个无符号数
采用遍历的方式发现很困难的时候，需要采取聪明一点的方式
1)如果遍历到e，那么之前不能有e，并且e不能再末尾
2)如果遍历到.,那么之前不能有.，并且之前不能有e
3)如果遍历到符号，那么如果之前有符号，只能够出现在e的后面，如果之前没符号，那么符号只能出现在第一位，或者出现在e的后面
4)如果遍历到不是上面所有的符号和0~9，返回False
"""
        hasE = False
        hasDot = False
        hasSign = False
        for i in range(len(s)):
            if s[i] == 'e' or s[i] == 'E':
                # 如果遍历到e，那么之前不能有e，并且e不能在末尾
                if hasE or i == len(s) - 1:
                    return False
                hasE = True
            # 如果遍历到.,那么之前不能有.，并且之前不能有e
            elif s[i] == '.':
                if hasDot or hasE:
                    return False
                hasDot = True
            # 如果遍历到符号
            # 1)那么如果之前有符号，只能够出现在e的后面
            # 2)如果之前没符号，那么符号只能出现在第一位，或者出现在e的后面
            elif s[i] == '+' or s[i] == '-':
                if hasSign and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
                if not hasSign:
                    if i != 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                        return False
                hasSign = True
            # 如果遍历到不是上面所有的符号和0~9，返回False
            else:
                if s[i] < '0' or s[i] > '9':
                    return False
        return True
