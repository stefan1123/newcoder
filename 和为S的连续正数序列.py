"""
题目描述
    小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
    但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,
    他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快
    的找出所有和为S的连续正数序列? Good Luck!
输出描述:
    输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
代码情况：accepted
"""

class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        # 0不是正整数，所以tsum至少大于等于3
        # 解法(滑窗)：由于是要找连续的正数，所以不妨设small,big = 1,2,若此时数组的和小于tsum时，
        # 把big+1加入到数组中，若是相等则找到，否则若是还小则继续big+1求和进行判断，若是较大，
        # 则丢掉数组最小值，继续判断。
        if tsum<3:
            return []
        elif tsum == 3:
            return [[1,2]]
        small,big=1,2
        # 最大的一个序列（两个数）为，[small, (tsum+1)//2],连续两个数之和一定是奇数，所以，
        # 如果这个序列是两个元素，则tsum一定是奇数
        middle = (tsum+1)>>1
        res = []
        curSum = small+big
        while small<middle:
            if curSum < tsum:
                big += 1
                curSum += big
            elif curSum > tsum:
                curSum -= small
                small += 1
            else:
                res.append(list(range(small,big+1)))
                curSum -= small
                small += 1
        return res
    
#        # 方法二：一样的思想，不同的写法
#        if tsum<3:
#            return []
#        elif tsum==  3:
#            return [[1,2]] # 一个序列也要是[[],] 格式
#        small,big=1,2
#        res = []
#        onepath = []
#        onepath.append(small)
#        onepath.append(big)
#        # 序列至少两个数字
#        while len(onepath)>=2:
#            if sum(onepath)<tsum:
#                onepath.append(onepath[-1]+1)
#                #continue
#            elif sum(onepath)>tsum:
#                onepath.pop(0)
#            else:
##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!     第二次犯错了  !!!!!!!!!!!!!!!!!!!
#                # 复制链表一定要用onepath[:],而不能是onepath
#                # res.append(onepath)
#                res.append(onepath[:])
#                onepath.pop(0)
#        return res

        
        

if __name__ == '__main__':
    num = 100
    s = Solution()
    ret = s.FindContinuousSequence(num)    
