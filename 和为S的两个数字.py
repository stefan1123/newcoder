"""
题目描述
    输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
    如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
    对应每个测试案例，输出两个数，小的先输出。
代码情况：accepted
"""

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
#        # 方法一：穷举，O(n^2)
#        if len(array)<=0:
#            return []
#        res = []
#        for i,a  in enumerate(array):
#            for j,b in enumerate(array[i+1:]):
#                if a+b == tsum:
#                    res.append((min(a,b),max(a,b)))
#        if len(res) <= 0:
#            return []
#        c,d = res[0][0],res[0][1]
#        m = c*d
#        for a,b in res[1:]:
#            if a*b < m:
#                c,d = a,b
#        return c,d
        
        # 方法二：移动两个指针: 从头，从尾，开始移动; O(N)
        # 如果两数和大于目标值，end指针往前移动；小于，start往后移动，否则找到。
        if len(array)<=0:
            return []
        start = 0
        end = len(array)-1
        while start<end:
            if array[start]+array[end] < tsum:
                start+=1
            elif array[start]+array[end] > tsum:
                end -= 1
            else:
                return array[start],array[end]
        return []

if __name__ == '__main__':
    arr = [1,2,4,7,11,13]
    num = 15
    s = Solution()
    ret = s.FindNumbersWithSum(arr,num)    
