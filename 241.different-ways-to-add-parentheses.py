#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#
from typing import List
# @lc code=start
ord_0 = ord('0')
op_set = {'+','-','*'}
class Solution:
    def calculate(self,num1, num2, op):
        if op=='+':
            return num1+num2
        if op=='-':
            return num1-num2
        return num1*num2

    def diffWaysToCompute(self, expression: str) -> List[int]:
        num = 0
        nums = list()
        ops = list()
        for char in expression:
            if char.isdigit():
                num = num*10+ord(char)-ord_0
            else:
                nums.append(num)
                ops.append(char)
                num = 0
        nums.append(num)
        l = len(nums)
        dp = [[None]*l for i in range(l)]
        for i in range(l):
            dp[i][i]=[nums[i]]
        for i in range(l-1):
            dp[i][i+1]=[self.calculate(nums[i],nums[i+1],ops[i])]
        for i in range(l-3,-1,-1):
            for j in range(i+2,l):
                r = list()
                for k in range(i,j):
                    op = ops[k]
                    left = dp[i][k]
                    right = dp[k+1][j]
                    for num_left in left:
                        for num_right in right:
                            r.append(self.calculate(num_left,num_right,op))
                dp[i][j] = r
        return dp[0][-1]


# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.diffWaysToCompute("2-1-1"),[0,2],False)
    test(sol.diffWaysToCompute("2*3-4*5"),[-34,-14,-10,-10,10],False)
    test(sol.diffWaysToCompute("2"),[2],False)
    test(sol.diffWaysToCompute("2+1"),[3],False)
    test(sol.diffWaysToCompute("2-1"),[1],False)
    test(sol.diffWaysToCompute("2*1"),[2],False)
    test(sol.diffWaysToCompute("2*1+3*5-4+6"),[-28,44,12,20,36,-40,56,12,20,20,36,20,36,44,-13,23,7,11,19,-40,56,-25,35,22,30,7,30,15,14,30,14,30,38,11,19,14,11,34,42,19,42,27],False)

# Accepted
# 25/25 cases passed (28 ms)
# Your runtime beats 94.66 % of python3 submissions
# Your memory usage beats 6.66 % of python3 submissions (14.6 MB)
