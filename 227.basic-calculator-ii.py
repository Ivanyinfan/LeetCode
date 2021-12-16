#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#
import math
# @lc code=start
ord_0 = ord('0')
op_set = {"+","-","*","/"}
class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        lastNum = 0
        lastOp = '+'
        currentNum = 0
        for i, char in enumerate(s):
            if char.isdigit():
                currentNum = currentNum*10+ord(char)-ord_0
            if char in op_set or i==len(s)-1:
                if lastOp == '+':
                    result = result + lastNum
                    lastNum = currentNum
                elif lastOp == '-':
                    result = result + lastNum
                    lastNum = -currentNum
                    currentNum = 0
                elif lastOp == '*':
                    lastNum = lastNum * currentNum
                elif lastOp == '/':
                    lastNum = math.trunc(lastNum/currentNum)
                lastOp = char
                currentNum = 0
        return result + lastNum

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
    test(sol.calculate("3+5*6"),33)
    test(sol.calculate("3+5*6+1"),34)

# Accepted
# 109/109 cases passed (84 ms)
# Your runtime beats 72.98 % of python3 submissions
# Your memory usage beats 90.69 % of python3 submissions (15.4 MB)
