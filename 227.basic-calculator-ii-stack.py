#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
from enum import Enum
class Sign(Enum):
    plus = 1
    minus = -1
    multiply = 2
    divide = 3

class Solution:
    ord_0 = ord('0')
    op_set = {"+","-","*","/"}

    def calculateLast(self, stack, num, sign):
        if sign==Sign.divide:
            if stack[-1]<0:
                num = -(-stack[-1]//num)
            else:
                num = stack[-1]//num
            stack.pop()
            sign=Sign.plus
        elif sign==Sign.multiply:
            if stack[-1]<0:
                num = -(-stack[-1]*num)
            else:
                num = stack[-1]*num
            stack.pop()
            sign=Sign.plus
        return num, sign
    
    def calculate(self, s: str) -> int:
        stack = list()
        num = 0
        sign = Sign.plus
        for i, char in enumerate(s):
            if char.isdigit():
                num = num*10 + ord(char)-Solution.ord_0
            elif char in Solution.op_set:
                num, sign = self.calculateLast(stack, num, sign)
                if char=='+':
                    stack.append(num*sign.value)
                    num = 0
                    sign = Sign.plus
                elif char=='-':
                    stack.append(num*sign.value)
                    num = 0
                    sign = Sign.minus
                elif char=='*':
                    stack.append(num*sign.value)
                    num = 0
                    sign = Sign.multiply
                elif char=='/':
                    stack.append(num*sign.value)
                    num = 0
                    sign = Sign.divide
        num, sign = self.calculateLast(stack, num, sign)
        return sum(stack)+sign.value*num

        
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.calculate("3+2*2"),7)
    test(sol.calculate(" 3/2 "),1)
    test(sol.calculate(" 3+5 / 2 "),5)
    test(sol.calculate("1+1+1+1"),4)
    test(sol.calculate("1-2*1+1+1"),1)
    test(sol.calculate("1+1+1-2*1"),1)
    test(sol.calculate("14-3/2"),13) # 103

# Accepted
# 109/109 cases passed (144 ms)
# Your runtime beats 17.31 % of python3 submissions
# Your memory usage beats 30.58 % of python3 submissions (15.8 MB)
