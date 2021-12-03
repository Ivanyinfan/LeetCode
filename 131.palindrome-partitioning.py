#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
from typing import List
# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        l = len(s)
        self.dp = [[None]*(l+1) for _ in range(l+1)]
        for i in range(l+1): self.dp[i][i] = True
        for i in range(l): self.dp[i][i+1] = True
        for i in range(l-2, -1, -1):
            for j in range(i+2,l+1):
                if s[i]==s[j-1] and self.dp[i+1][j-1]:
                    self.dp[i][j]=True
                else:
                    self.dp[i][j]=False
        r = list()
        self.backTrack(s, 0, [0], r)
        for path in r:
            for i in range(1, len(path)):
                path[i-1] = s[path[i-1]:path[i]]
            path.pop()
        return r
        
                
    def backTrack(self, s, start, path:list, result):
        l = len(s)
        if start==l:
            result.append(path.copy())
            return
        for i in range(start+1, l+1):
            if self.dp[start][i]:
                path.append(i)
                self.backTrack(s, i, path, result)
                path.pop()
        
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.partition("aab"), [["a","a","b"],["aa","b"]])
    test(sol.partition('a'),[['a']])
    test(sol.partition('aaa'),[['a','a','a'],['a','aa',], ['aa','a'],['aaa']])

# Accepted
# 32/32 cases passed (760 ms)
# Your runtime beats 31.37 % of python3 submissions
# Your memory usage beats 5.79 % of python3 submissions (34.7 MB)
