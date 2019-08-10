"""
题目描述
  给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
代码情况：accepted
"""
class Solution:
    def multiply(self, A):
        # write code here
#        # 方法一，暴力相乘，O(n^2)
#        if len(A) <= 0:
#            return -1
#        elif len(A) == 1:
#            # 数组A只有一个数字时，只需要返回一个与A[0]不等的数组
#            return A[0]+1
#        
#        def _mul(arr):
#            res = 1
#            for i in range(len(arr)):
#                res *= arr[i]
#            return res
#        
#        B = [0 for i in range(len(A))]
#        for i in range(len(B)):
#            B[i] = _mul(A[:i]+A[i+1:])
#        return B   
        # 方法二： B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]
        # 分两端，前半段是前i个数的乘积（A[0]*A[1]*...*A[i-1]），可以从i=0 
        # 开始累积一个数形成B[i]前半段；后半段反向累积；前后两端对应相乘
        if len(A) <= 0:
            return []
        length = len(A)
        B = [1 for i in range(length)] # 正序累积
        ad = [1 for i in range(length)] # 反向累积
        # 前半段 B[i]=A[0]*A[1]*...*A[i-1] 的累积
        for i in range(1,length):
            B[i] = B[i-1]*A[i-1]
#        back = 1 # 暂时保存反向累乘的结果（累积）
        for j in range(length-2,-1,-1):
            ad[j] = ad[j+1]*A[j+1]
            B[j]*=ad[j]   # 前后半段的累积相乘     
#            back *= A[j+1]
#            B[j] *= back
        return B

if __name__ == '__main__':
    a = [5,7,2,8,3]
    res = Solution().multiply(a)

