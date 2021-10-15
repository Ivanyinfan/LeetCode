#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
from typing import List

from utils import test
# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=-1
        for i, t in enumerate(tokens):
            if t=='+':
                tokens[s-1]=tokens[s-1]+tokens[s]
                s = s - 1
            elif t=='-':
                tokens[s-1]=tokens[s-1]-tokens[s]
                s = s - 1
            elif t=='*':
                tokens[s-1]=tokens[s-1]*tokens[s]
                s = s - 1
            elif t=='/':
                sign = 1 if tokens[s-1]*tokens[s]>=0 else -1
                tokens[s-1]=abs(tokens[s-1])//abs(tokens[s])*sign
                s = s - 1
            else:
                s = s+1
                tokens[s]=int(t)
        return tokens[0]

        
# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    test(sol.evalRPN(["2"]),2)
    test(sol.evalRPN(["2","1","+"]),3)
    test(sol.evalRPN(["2","1","+","3","*"]),9)
    test(sol.evalRPN(["4","13","5","/","+"]),6)
    test(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]),22)

# Accepted
# 20/20 cases passed (85 ms)
# Your runtime beats 37.48 % of python3 submissions
# Your memory usage beats 45.96 % of python3 submissions (14.6 MB)
