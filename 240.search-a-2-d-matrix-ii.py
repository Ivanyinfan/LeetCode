#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
from typing import List
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_num, column_num = len(matrix), len(matrix[0])
        row_start, row_end, column_start, column_end=0,row_num,0,column_num
        while row_start<row_end and column_start<column_end:
            if target==matrix[row_start][column_end-1]:
                return True
            if target==matrix[row_end-1][column_start]:
                return True
            # if target>matrix[row_start][column_end-1]:
            #     row_start+=1
            # elif target>matrix[row_end-1][column_start]:
            #     column_start+=1
            # elif target<matrix[row_end-1][column_start]:
            #     row_end-=1
            # elif target<matrix[row_start][column_end-1]:
            #     column_end-=1
            if target>matrix[row_start][column_end-1]:
                row_start+=1
            else:
                column_end-=1
            if target>matrix[row_end-1][column_start]:
                column_start+=1
            else:
                row_end-=1
        return False
# @lc code=end
from utils import test
def testMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            test(sol.searchMatrix(matrix, matrix[i][j]), True)
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    testMatrix(matrix)
    test(sol.searchMatrix(matrix, 20), False)
    test(sol.searchMatrix(matrix, 25), False)
    test(sol.searchMatrix(matrix, 0), False)
    matrix = [[1]]
    test(sol.searchMatrix(matrix, 1), True)
    test(sol.searchMatrix(matrix, 0), False)
    matrix = [[5,6,9],[9,10,11],[11,14,18]]
    test(sol.searchMatrix(matrix, 9), True) # 69
    testMatrix(matrix)

# Accepted
# 129/129 cases passed (275 ms)
# Your runtime beats 10.05 % of python3 submissions
# Your memory usage beats 92.71 % of python3 submissions (20.5 MB)
