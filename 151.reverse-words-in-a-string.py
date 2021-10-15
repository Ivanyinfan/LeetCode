#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#
from utils import test
# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    test(sol.reverseWords("the sky is blue"),"blue is sky the")
    test(sol.reverseWords("  hello world  "),"world hello")
    test(sol.reverseWords("a good   example"),"example good a")
    test(sol.reverseWords("  Bob    Loves  Alice   "),"Alice Loves Bob")
    test(sol.reverseWords("Alice does not even like bob"),"bob like even not does Alice")

# Accepted
# 57/57 cases passed (64 ms)
# Your runtime beats 10.63 % of python3 submissions
# Your memory usage beats 86.35 % of python3 submissions (14.2 MB)
