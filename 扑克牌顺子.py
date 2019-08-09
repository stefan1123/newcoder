"""
题目描述
    LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
    他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
    “红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小王可以
    看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作
    2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我
    们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。
代码情况：accepted

"""

class Solution:
    # 抽5张牌，numbers是5个数字
    def IsContinuous(self, numbers):
#        # write code here
        # 方法一：1、排序
        #        2、计算所有相邻数字间隔总数
        #        3、计算0的个数
        #        4、如果2、3相等，就是顺子
        #        5、如果出现对子，则不是顺子
        if len(numbers)!=5:
            return False
        # 排序
        self.quicksort(numbers)
        #numbers.sort()
        # 查找0的个数
        numofzero = 0
        for n in numbers:
            if n == 0:
                numofzero += 1
        # 查找数组前后两个元素之间缺几个数字，
        # 如2，4之间，缺4-2-1个数字，即数字3
        # 如果碰上有相等的元素，则不能构成顺子
        # === note ====
        # 由于有0存在，可能存在多个0，需要从最后一个0之后开始判断是否有元素相等
        numofgap = 0
#        print('numofzero:',numofzero)
        low = numofzero
        high = low+1
        while high<len(numbers):
#            print('low',low)
            if numbers[low] == numbers[high]:
                return False
            numofgap += numbers[high]-numbers[low]-1
            low = high 
            high += 1
        return True if numofzero>=numofgap else False
         
    def quicksort(self,arr):
        if len(arr)<=0:
            return
        def _sort(arr,low,high):
            if low>high:
                return
            p = patition(arr,low,high)
            _sort(arr,low,p-1)
            _sort(arr,p+1,high)
             
        def patition(arr,start,end):
            tmp = arr[start]
            low = start
            high = end
            while low<high:
                while low<high and arr[high]>=tmp:
                    high -= 1
                arr[low],arr[high] = arr[high],arr[low]
                while low<high and arr[low]<=tmp:
                    low += 1
                arr[low],arr[high] = arr[high],arr[low]
            return low
        _sort(arr,0,len(arr)-1)

        
if __name__ == '__main__':
    arr = [4,3,0,0,7]
    s = Solution()
    res = s.IsContinuous(arr) 
