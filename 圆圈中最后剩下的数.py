"""
题目描述
    0,1,...n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个
    圆圈里剩下的最后一个数字。（约瑟夫环问题）
代码情况：accepted
"""

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        # 方法一：用数组充当链表环
        # 考虑一种情况，如果第m个数字不删除，每次只做访问，则有，每次的数组的索引为当前索引i加上
        # m-1（为什么是m-1，原因是，从i开始数m个的话，除了索引为i的这一位，还应往后数m-1位），
        # 由于是原来的问题数组是一个环，所以，无论从哪个索引位开始数，都要对环长取模，即(m-1+i)%len.
        # 本题由于访问到的数字要删除，于是稍加改变即可，每次取变换后的数组（圆环）的长度进行模计算即可。
        if n<0 or m<1:
            return -1
        res = list(range(n))
        i = 0
        while len(res)>1:
            i = (m+i-1)%len(res)
            res.pop(i)
        return res[0]
        
#        # 访问圆环（不做删除的情况）
#        for j in range(3):
#            i = (m-1+i)%len(res)
#            print(res[i])
#            i+=1 # 由于没删除该index=i的数，所以移到下一位作为下一次循环的开始
            
        return res
