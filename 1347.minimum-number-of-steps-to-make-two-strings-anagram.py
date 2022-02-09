#
# @lc app=leetcode id=1347 lang=python3
#
# [1347] Minimum Number of Steps to Make Two Strings Anagram
#
from collections import Counter
# @lc code=start
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter = Counter(s)
        result = 0
        for char in t:
            fre = counter.get(char, 0)
            if fre!=0:
                counter[char]=fre-1
            else:
                result+=1
        return result
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.minSteps(s = "bab", t = "aba"), 1)
    test(sol.minSteps(s = "leetcode", t = "practice"), 5)
    test(sol.minSteps(s = "anagram", t = "mangaar"), 0)

# Accepted
# 63/63 cases passed (288 ms)
# Your runtime beats 44.67 % of python3 submissions
# Your memory usage beats 96.26 % of python3 submissions (14.6 MB)
