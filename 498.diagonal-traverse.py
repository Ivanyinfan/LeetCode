#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#
from typing import List
# @lc code=start
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m,n = len(mat), len(mat[0])
        result = list()
        for i in range(m+n):
            x_start = max(0, i-m+1)
            x_end = min(n-1, i)
            step = 1
            if i&1:
                x_start, x_end, step = x_end, x_start-1, -step
            else:
                x_end += 1
            for x in range(x_start, x_end, step):
                y = i-x
                result.append(mat[y][x])
        return result

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]),[1,2,4,7,5,3,6,8,9])
    test(sol.findDiagonalOrder([[1,2],[3,4]]),[1,2,3,4])
    test(sol.findDiagonalOrder([[1]]),[1])
    test(sol.findDiagonalOrder([[1,2,3],[4,5,6]]),[1,2,4,5,3,6])

# Accepted
# 32/32 cases passed (221 ms)
# Your runtime beats 54.21 % of python3 submissions
# Your memory usage beats 42.98 % of python3 submissions (17.1 MB)
