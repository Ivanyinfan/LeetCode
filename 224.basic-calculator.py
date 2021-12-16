#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    ord_0 = ord('0')
    def calculate(self, s: str) -> int:
        stack = list()
        i = 0
        num = 0
        sign = 1
        result = 0
        for i, char in enumerate(s):
            if char.isdigit():
                num = num*10+ord(s[i])-Solution.ord_0
            elif char=='+':
                result += sign*num
                num = 0
                sign = 1
            elif char=='-':
                result += sign*num
                num = 0
                sign = -1
            elif char=='(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
                num = 0
            elif char==")":
                result += sign*num
                pre_sign = stack.pop()
                pre_result = stack.pop()
                result = pre_result + pre_sign*result
                num = 0
                sign = 1
        return result + sign*num
                    
            
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.calculate("1 + 1"),2)
    test(sol.calculate(" 2-1 + 2 "),3)
    test(sol.calculate("(1+(4+5+2)-3)+(6+8)"),23)
    test(sol.calculate("(1+(1+(1+1)))"),4)
    test(sol.calculate("(1-(1-(1-1)))"),0)
    test(sol.calculate("1+(1+1)"),3)

# Accepted
# 42/42 cases passed (80 ms)
# Your runtime beats 71.45 % of python3 submissions
# Your memory usage beats 95.58 % of python3 submissions (15.2 MB)
