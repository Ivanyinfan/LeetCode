#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = dict()
        visited = set()
        for i, char in enumerate(s):
            if char in char_map:
                if t[i]!=char_map[char]:
                    return False
            else:
                if t[i] in visited:
                    return False
                char_map[char] = t[i]
                visited.add(t[i])
        return True
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.isIsomorphic("egg","add"), True)
    test(sol.isIsomorphic("foo","bar"), False)
    test(sol.isIsomorphic("paper","title"), True)
    test(sol.isIsomorphic("abcd","bcda"), True)

# Accepted
# 43/43 cases passed (36 ms)
# Your runtime beats 90.86 % of python3 submissions
# Your memory usage beats 69.14 % of python3 submissions (14.4 MB)
