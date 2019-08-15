"""
题目描述
    求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包
    含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,
    并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
代码情况：accepted
"""

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        # 方法一： 暴力查找
#        if n == 1:
#            return 1
#        elif not n or n < 1:
#            return 0
#        else:
#            cnt = 0
#            for num in range(1,n+1):
#                while num>0:
#                    mod = num%10
#                    if mod == 1:
#                        cnt += 1
#                    num =num//10
#            return cnt
        
        # 方法二：找规律，数学归纳法得出：
        # 设找第i位（i从右开始，以1开始计算）上的1的个数
        # k= num % 10^i 
        # count = (num // 10^i)*( 10^(i-1) ) + if (k>2*10^(i-1)-1) 1 else if(k<10^(i-1)) 0 else k-10^(i-1)+1
        if n == 1:
            return 1
        elif not n or n < 1:
            return 0
        # 为了方便计算，把数字转换为str
        length = len(str(n))
        s = 0
        # 注意，此处的索引从0开始
        for i in range(length):
            s += self.getnumof1_eachlocation(n,i)
        return s
            
    def getnumof1_eachlocation(self,num,i):
        times = pow(10,i)
        base = (num // pow(10,i+1))*times
        k = num % pow(10,i+1)
        aux = 0
        if k>2*times-1:
            aux = times
        elif k<times:
            aux = 0
        else:
            aux = k-times+1
        return base+aux
        
if __name__ == "__main__":
    s = Solution()
    n = 12
    res = s.NumberOf1Between1AndN_Solution(n)
    
