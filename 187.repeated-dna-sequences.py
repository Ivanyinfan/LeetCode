#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#
from typing import List
# @lc code=start
class Solution:
    digit_map = {'A':1,'C':2,'G':3,'T':4}
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        r = list()
        if len(s)<11: return r
        visited = dict()
        num = 0
        for i in range(9):
            num = num*10+Solution.digit_map[s[i]]
        for i in range(9, len(s)):
            num = num%1000000000*10+Solution.digit_map[s[i]]
            if num in visited:
                visited[num][1]+=1
            else:
                visited[num]=[i, 1]
        for val in visited.values():
            if val[1]>1:
                r.append(s[val[0]-9:val[0]+1])
        return r


# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"), ["AAAAACCCCC","CCCCCAAAAA"])
    test(sol.findRepeatedDnaSequences("AAAAAAAAAAAAA"), ["AAAAAAAAAA"])

# Accepted
# 31/31 cases passed (80 ms)
# Your runtime beats 41.43 % of python3 submissions
# Your memory usage beats 5.04 % of python3 submissions (36.3 MB)
