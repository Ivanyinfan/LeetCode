#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        if not num: return num
        return 1+(num-1)%9
# @lc code=end

# Accepted
# 1101/1101 cases passed (32 ms)
# Your runtime beats 72.57 % of python3 submissions
# Your memory usage beats 45.64 % of python3 submissions (14.3 MB)
