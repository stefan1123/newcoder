"""
题目描述
    给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组
    {2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别
    为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： 
    {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， 
    {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
代码情况：accepted
"""

class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if len(num)<1 or len(num)<size or size<1:
            return []
        res = []
        low = 0
        high = low+size-1
        length = len(num)
        while high<length:
            tmp = num[low:high+1]
            #print(tmp)
            res.append(max(tmp))
            low+=1
            high += 1
        return res
        
if __name__ == "__main__":
    s = Solution()
    n = [2,3,4,2,6,2,5,1]
    res = s.maxInWindows(n,3)
