/*
题目描述
  写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
代码：acc

解释：由于python会自动处理溢出（负数相加的时候），所以需要对溢出进行处理，麻烦，而c++没有溢出这个问题。
python版本可以参考 https://www.jianshu.com/p/21fd1598d4ae
*/

class Solution {
public:
    int Add(int num1, int num2)
    {
        int sum,carry;
        while (num2!=0)
        {
            // 利用异或运算来计算不带进位的加法结果
            sum = num1^num2;
            // 利用与运算计算进位的标志，并向左移动一位相加（即异或），直到进位为0
            carry = (num1&num2)<<1;
            num1 = sum;
            num2 = carry;
        }
        return num1;
    }
};
