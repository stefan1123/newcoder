"""
题目描述
    一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
代码情况：accepted
"""

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
#        # 方法一：hashmap
#        if len(array) <= 0:
#            return None
#        res = []
#        hashmap = {}
#        for n in array:
#            if n not in hashmap.keys():
#                hashmap[n] = 0
#            hashmap[n] += 1
#        for num in hashmap.keys():
#            if hashmap[num] == 1:
#                res.append(num)
#        return res
        
        # 方法二（推荐）：使用数字的二进制的异或，即一个数与自己异或一定为0，一个非0数和0异或还是它本身
        # 基础：比如 [2,4,2], 按位以后符号 “^”
        # 2 ^ 4 ^ 2  ?= 2 ^ 2 ^ 4
        # 2(0010) ^ 4(0100) ^ 2(0010) = 4(0100),括号内为相应二进制
        # 解法：如果两个数字不同，异或的结果中一定存在二进制位为1，暂且取倒数第一位（即从低位开始查找二进制位）为1的索引为分类标准，
        # 即根据该标准为是否相同将数字分为两组，其中，相同的数字一定在同一组，因为其二者二进制一样，不同的数字一定不在一组，
        # 由于相同的数组的出现次数为偶数，异或之后的二进制结果为全0，因此，每组剩下的数字即为只出现一次的数字。
        if len(array) <= 0:
            return None
        s = 0
        # 依次异或一边，找到只出现依次的两个数的异或结果
        for num in array:
            s = s^num
        # 取分类标准的索引
        idx = 0
        while s&1 == 0: # 即最后一位是0
            s = s>>1
            idx += 1
        a = 0
        b = 0
        for n in array:
            if  self.isBit(n,idx):
                a ^= n # 分类索引为True的一组中，剩下的即为出现奇数次的数
            else:
                b ^= n
        return [a,b]

    def isBit(self,num,index):
        num = num >> index
        return num&1 
