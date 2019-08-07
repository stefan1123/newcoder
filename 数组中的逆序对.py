# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 16:41:08 2019

@author: xiang
"""

"""
题目描述(acc)
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出
这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

输入描述:
    题目保证输入的数组中没有的相同的数字   
    数据范围：
    	对于%50的数据,size<=10^4
    	对于%75的数据,size<=10^5
    	对于%100的数据,size<=2*10^5
    
示例1
    输入
        1,2,3,4,5,6,7,0
    输出
        7
"""

class Solution:
    def __init__(self):
        self.count = 0
        

    def mergeSort(self, data):
        # 设递归停止条件
        if len(data) <= 1:
            return data
        n = len(data)
        # 进行归并的二分
        mid = n//2
        left = self.mergeSort(data[:mid])
        right = self.mergeSort(data[mid:])
        
        # 进行归并
        i = 0
        j = 0
        res = []
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                # 无逆序对，只进行归并排序
                res.append(left[i])
                i += 1
            else:
                # 有逆序对，先排序，再计算逆序对的数目
                res.append(right[j])
                self.count+=(len(left)-1)-i+1
                j += 1
        return res+left[i:]+right[j:]
        
    def InversePairs(self, data):
        # write code here
        if len(data) < 2: 
            return 0
        # 使用归并排序
        # 在归并过程中，依次比较前半部分与后半部分的值，如果前半部分的值大于后半部分的值，则
        # 逆序对数为前半部分的该值到前半部剩余的值的总个数，即 len(left)-i,(index=i的值
        # 大于后半部的某个数)
        self.mergeSort(data)
        
        # 牛客网上要求输出要对1000000007取模
        return self.count % 1000000007
                
            
if __name__ == '__main__':
    
    data=[1,2,3,4,5,6,7,0]
    s = Solution()
    res = s.InversePairs(data)
    print(res)
