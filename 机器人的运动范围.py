"""
题目描述
    地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个
    方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够
    进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
    请问该机器人能够达到多少个格子？
代码情况：accepted
"""

class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        # 经典的回溯法。
        # 此题为必须找出所有符合要求的坐标。而不是找到一个即返回
        if threshold<0 or rows<1 or cols<1:
            return 0
        # 记录该位置是否已经被访问过
        visited = [False] * (rows*cols)
        self.coor = []   
        cnt = self.movingCore(threshold,rows,cols,0,0,visited) 
        print(self.coor)
        return cnt
        
    def movingCore(self,thresh, row, col, i, j, visited):
        cnt = 0        
        if self.check(thresh,row,col,i,j,visited):
            visited[i*col+j]=True
            self.coor.append([i,j])
            # 统计所有符合要求的点（即找出所有符合要求的方格）
            cnt = 1 + self.movingCore(thresh,row,col,i-1,j,visited)\
            +self.movingCore(thresh,row,col,i+1,j,visited)\
            +self.movingCore(thresh,row,col,i,j-1,visited)\
            +self.movingCore(thresh,row,col,i,j+1,visited)
        return cnt
        
    def check(self,thresh, row, col, i, j, visit):
        # 在边界内且没被访问过
        if i<row and i>=0 and j<col and j>=0 and not visit[i*col+j]:
            # 符合小于阈值的条件
            if self.getSum(i)+self.getSum(j) <= thresh:
                return True
        return False
            
    def getSum(self,num):
        s = 0
        while num>0:
            mod = num % 10
            s += mod
            num = num // 10            
        return s


if __name__ == "__main__":
    s = Solution()
    res = s.movingCount(2,3,3)
