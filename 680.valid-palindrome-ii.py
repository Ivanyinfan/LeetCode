#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome2(self, s, start, end):
        while start<end:
            if s[start]!=s[end]:
                return start, end
            start += 1
            end -= 1
        return None

    def validPalindrome(self, s: str) -> bool:
        l = len(s)
        r = self.validPalindrome2(s, 0, l-1)
        if r==None:
            return True
        return self.validPalindrome2(s, r[0]+1, r[1])==None or \
            self.validPalindrome2(s, r[0], r[1]-1)==None
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.validPalindrome("aba"), True)
    test(sol.validPalindrome("abca"), True)
    test(sol.validPalindrome("abc"), False)
    test(sol.validPalindrome("a"), True)
    test(sol.validPalindrome("ab"), True)

# Accepted
# 467/467 cases passed (184 ms)
# Your runtime beats 37.15 % of python3 submissions
# Your memory usage beats 73.02 % of python3 submissions (14.6 MB)
