#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    orda = ord('a')
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for str in strs: group[self.strToTuple(str)].append(str)
        return list(group.values())

    def strToTuple(self, str):
        r = [0]*26
        for char in str: r[ord(char)-Solution.orda]+=1
        return tuple(r)
# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(sol.groupAnagrams([""]))
    print(sol.groupAnagrams(["",'']))

# Accepted
# 115/115 cases passed (120 ms)
# Your runtime beats 42.81 % of python3 submissions
# Your memory usage beats 23.33 % of python3 submissions (19.1 MB)
