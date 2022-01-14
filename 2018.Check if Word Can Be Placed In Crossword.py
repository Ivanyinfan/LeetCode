#
# @lc app=leetcode id=2018 lang=python3
#
# [2018] Check if Word Can Be Placed In Crossword
#
from typing import List
# @lc code=start
dirs = [[-1,0],[1,0],[0,-1],[0,1]]
class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        l = len(word)
        for i in range(m):
            for j in range(n):
                if board[i][j]==' ' or board[i][j]==word[0]:
                    for dir in dirs:
                        ni,nj = i-dir[0],j-dir[1]
                        if ni!=-1 and ni!=m and nj!=-1 and nj!=n and board[ni][nj]!='#':continue
                        endi, endj = i+dir[0]*l, j+dir[1]*l
                        if endi>m or endi<-1 or endj>n or endj<-1: continue
                        if endi!=-1 and endi!=m and endj!=-1 and endj!=n and board[endi][endj]!='#':continue
                        index = 1
                        ni,nj = i+dir[0],j+dir[1]
                        while index<l:
                            if board[ni][nj]!=' ' and board[ni][nj]!=word[index]:
                                break
                            index += 1
                            ni,nj = ni+dir[0], nj+dir[1]
                        if index==l:
                            return True
        return False


# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.placeWordInCrossword(board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"), True)
    test(sol.placeWordInCrossword(board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"), False)
    test(sol.placeWordInCrossword(board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"), True)

# Success
# Runtime: 1908 ms, faster than 25.58% of Python3 online submissions for Check if Word Can Be Placed In Crossword.
# Memory Usage: 26.5 MB, less than 63.72% of Python3 online submissions for Check if Word Can Be Placed In Crossword.
