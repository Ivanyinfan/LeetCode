#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        leftCount = rightCount = 0
        result = list()
        for i, char in enumerate(s):
            if char == '(':
                leftCount += 1
                result.append(char)
            elif char == ')':
                if leftCount>0:
                    leftCount-=1
                    result.append(char)
            else:
                result.append(char)
        l = len(result)
        i = l-1
        for j in range(l-1, -1, -1):
            char = result[j]
            if char == '(':
                if rightCount > 0:
                    rightCount -= 1
                    result[i]=char
                    i -= 1
            elif char == ')':
                rightCount += 1
                result[i]=char
                i -= 1
            else:
                result[i]=char
                i -= 1
        return ''.join(result[i+1:])



# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.minRemoveToMakeValid("lee(t(c)o)de)"),"lee(t(c)o)de")
    test(sol.minRemoveToMakeValid("a)b(c)d"),"ab(c)d")
    test(sol.minRemoveToMakeValid("))(("),"")
    test(sol.minRemoveToMakeValid("()"),"()")
    test(sol.minRemoveToMakeValid("("),"")
    test(sol.minRemoveToMakeValid(")"),"")

# Accepted
# 62/62 cases passed (184 ms)
# Your runtime beats 30.66 % of python3 submissions
# Your memory usage beats 12.34 % of python3 submissions (17 MB)
