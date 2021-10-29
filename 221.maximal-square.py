#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
from typing import List
# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [0] + [int(e) for e in matrix[0]]
        r = int(any(dp))
        for i in range(1,len(matrix)):
            ndp = [None]*len(dp)
            ndp[0]=0
            for j in range(len(matrix[i])):
                if matrix[i][j]=='0': ndp[j+1]=0
                else:
                    ndp[j+1]=min([ndp[j], dp[j], dp[j+1]])+1
                    r = max(r, ndp[j+1])
            dp = ndp
        return r*r
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]),4)
    test(sol.maximalSquare([["0","1"],["1","0"]]),1)
    test(sol.maximalSquare([["0"]]),0)

# Accepted
# 75/75 cases passed (196 ms)
# Your runtime beats 91.61 % of python3 submissions
# Your memory usage beats 27.35 % of python3 submissions (15.7 MB)
