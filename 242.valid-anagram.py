#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
ord_a = ord('a')
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        letter_count = [0]*26
        for char in s: letter_count[ord(char)-ord_a]+=1
        for char in t: letter_count[ord(char)-ord_a]-=1
        return not any(letter_count)
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.isAnagram("anagram","nagaram"),True)
    test(sol.isAnagram("rat","car"),False)

# Accepted
# 36/36 cases passed (71 ms)
# Your runtime beats 18.58 % of python3 submissions
# Your memory usage beats 56.65 % of python3 submissions (14.6 MB)
