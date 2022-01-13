#
# @lc app=leetcode id=1284 lang=python3
#
# [1284] Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
#
from typing import List
from collections import deque
import copy
# @lc code=start
class Solution:
    dir = [[-1,0],[0,1],[0,0],[1,0],[0,-1]]

    def encode(self, mat):
        result = 0
        for i in range(self.m):
            for j in range(self.n):
                result = result|((mat[i][j]&1)<<(i*self.m+j))
        return result

    def decode(self, integer):
        mat = [[None]*self.n for i in range(self.m)]
        for i in range(self.count):
            index = self.count - i - 1
            x,y=index//self.m, index-index//self.m*self.m
            mat[x][y]=(integer&(1<<i))>>i
        return mat

    def flip(self,mat,x,y):
        newMat = copy.deepcopy(mat)
        for d in Solution.dir:
            newx,newy = x+d[0],y+d[1]
            if 0<=newx and newx<self.m and 0<=newy and newy<self.n:
                newMat[newx][newy]^=1
        return newMat

    def minFlips(self, mat: List[List[int]]) -> int:
        self.m,self.n = len(mat), len(mat[0])
        self.count = self.m*self.n
        root = self.encode(mat)
        stack = deque([[root,mat]])
        visited = {root}
        level = 0
        while stack:
            num = len(stack)
            while num>0:
                number, matrix = stack.popleft()
                if number==0:
                    return level
                for i in range(self.m):
                    for j in range(self.n):
                        newMat = self.flip(matrix,i,j)
                        newNum = self.encode(newMat)
                        if newNum not in visited:
                            visited.add(newNum)
                            stack.append([newNum,newMat])
                num -= 1
            level += 1
        return -1



# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.minFlips([[0,0],[0,1]]),3)
    test(sol.minFlips([[0]]),0)
    test(sol.minFlips([[1,0,0],[1,0,0]]),-1)
    test(sol.minFlips([[1,0,0]]),2)

# Accepted
# 26/26 cases passed (455 ms)
# Your runtime beats 7.02 % of python3 submissions
# Your memory usage beats 24.17 % of python3 submissions (14.5 MB)
