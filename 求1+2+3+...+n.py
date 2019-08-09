"""
题目描述
    求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、
    case等关键字及条件判断语句（A?B:C）。意义不大。
代码情况：accepted
"""

class Solution:
    def __init__(self):
        self.sum = 0
    def Sum_Solution(self, n):
        # write code here
        # 方法：定义一个类属性sum，然后递归向下，sum+n, n自减
        def _sum(x):
            self.sum += x
            x -= 1
            # 漂亮的写法，用大于小于和与操作做判断
            return x>0 and _sum(x)
        
        _sum(n)
        
        return self.sum

        
if __name__ == '__main__':
    m = 3
    s = Solution()
    res = s.Sum_Solution(m) 
        
