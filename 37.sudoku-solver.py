#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
from typing import List
# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row,column,grid = [0]*9,[0]*9,[0]*9
        gridIndex = lambda x,y:x//3*3+y//3
        empty = list()
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    empty.append([i,j,0])
                else:
                    e = int(board[i][j])
                    mask = 1<<e
                    row[i]|=mask
                    column[j]|=mask
                    grid[gridIndex(i,j)]|=mask
        c = 0
        while c!=len(empty) and c!=-1:
            if empty[c][-1]!=0:
                mask = ~(1<<empty[c][-1])
                row[empty[c][0]]&=mask
                column[empty[c][1]]&=mask
                grid[gridIndex(empty[c][0], empty[c][1])]&=mask
            s = empty[c][-1] + 1
            for i in range(s,10,1):
                mask = 1<<i
                if row[empty[c][0]]&mask: continue
                if column[empty[c][1]]&mask: continue
                if grid[gridIndex(empty[c][0], empty[c][1])]&mask: continue
                empty[c][-1] = i
                row[empty[c][0]]|=mask
                column[empty[c][1]]|=mask
                grid[gridIndex(empty[c][0], empty[c][1])]|=mask
                break
            else:
                empty[c][-1] = 0
                c = c - 1
                continue
            c = c + 1
        for e in empty: board[e[0]][e[1]]=str(e[-1])
        return board

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    input = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    output = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
    test(sol.solveSudoku(input), output)

# Accepted
# 6/6 cases passed (196 ms)
# Your runtime beats 70.34 % of python3 submissions
# Your memory usage beats 89.06 % of python3 submissions (14.3 MB)
