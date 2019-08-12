"""
题目描述
    如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序
    之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两
    个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的
    中位数。
代码情况：accepted
note：self.GetMedian()必须有参数，否则报错，坑！
"""

class Solution:
    def __init__(self):
        self.data = []
    def Insert(self, num):
        # write code here
        self.data.append(num)
    
    def GetMedian(self,n):
    # 注意：除了self之外必须要有一个参数。或许是为了可以直接self.GetMedian(datastream)??
    # def GetMedian(self):
        # write code here
        self.data.sort()
        length = len(self.data)
        # mid = length>>1
        mid = int(length//2)
        if length % 2 == 0:            
            return (self.data[mid]+self.data[mid-1])/2.0
        else:
            return self.data[mid]    
        
if __name__ == "__main__":
    s = Solution()
    for i in range(10,0,-3):
        s.Insert(i)
    print(s.data)
    print(s.GetMedian(s.data))
