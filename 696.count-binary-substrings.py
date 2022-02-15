#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        current = 0
        result = 0
        l = len(s)
        for i, char in enumerate(s):
            current += 1
            if i==l-1 or char!=s[i+1]:
                result+=min(prev, current)
                prev,current = current, 0
        return result

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.countBinarySubstrings("00110011"), 6)
    test(sol.countBinarySubstrings("10101"), 4)
    test(sol.countBinarySubstrings("000111"), 3)
    test(sol.countBinarySubstrings("111000"), 3)
    test(sol.countBinarySubstrings("111000111"), 6)
    test(sol.countBinarySubstrings("1"), 0)
    test(sol.countBinarySubstrings("0"), 0)
    test(sol.countBinarySubstrings("10"), 1)

# Accepted
# 91/91 cases passed (230 ms)
# Your runtime beats 52.36 % of python3 submissions
# Your memory usage beats 89.74 % of python3 submissions (14.4 MB)
