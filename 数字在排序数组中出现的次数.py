"""
数字在排序数组中出现的次数
题目描述(acc)
  统计一个数字在排序数组中出现的次数。
"""
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
#        # 方法一：hashmap,时间复杂度O(n)
#        if len(data) <= 0:
#            return 0
#        hashmap = {}
#        for i in data:
#            if i not in hashmap.keys():
#                hashmap[i]=0
#            hashmap[i]+=1
#        return hashmap[k] if k in hashmap.keys() else 0
        
        # 方法二：二分查找,时间复杂度O(log(n))
        if not data:
            return 0
        if len(data) == 1 and data[0] != k:
            return 0
        
        # 二分查找的循环写法
        left = 0
        right = len(data) - 1
        first_k = 0
        while left <= right:
            mid = (left + right) // 2
            if data[mid] < k:
                left = mid + 1
            elif data[mid] > k:
                right = mid - 1
            else:
                if mid == 0:
                    first_k = 0
                    break
                elif data[mid-1] != k:
                    first_k = mid
                    break
                else:
                    # 去mid前面找第一个K
                    right = mid - 1       
        left = 0
        right = len(data) - 1
        last_k = -1
        while left <= right:
            mid = (left + right) // 2
            if data[mid] < k:
                left = mid + 1
            elif data[mid] > k:
                right = mid - 1
            else:               
                if mid == len(data) - 1:
                    last_k = len(data) - 1
                    break
                elif data[mid+1] != k:
                    last_k = mid
                    break
                else:
                    # 去mid后面找K
                    left = mid + 1       
        return last_k - first_k + 1
