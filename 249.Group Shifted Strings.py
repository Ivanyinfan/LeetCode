#
# @lc app=leetcode id=249 lang=python3
#
# [249] Group Shifted Strings
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        resultMap = defaultdict(list)
        for string in strings:
            tmp = [None]*len(string)
            base = ord(string[0])
            for i, char in enumerate(string):
                tmp[i] = ord(char) - base
            resultMap[tuple(tmp)].append(string)
        return resultMap.values()

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.groupStrings(strings = ["abc","bcd","acef","xyz","az","ba","a","z"]), [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]], ordered=False)
    test(sol.groupStrings(strings = ["a"]), [['a']], ordered=False)