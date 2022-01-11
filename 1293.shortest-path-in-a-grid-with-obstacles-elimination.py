#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        minimum = m+n-2
        if k>=minimum: return minimum
        target = (m-1,n-1)
        state = (0,0,k)
        queue = deque([state])
        grid[0][0]=2
        length = 0
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = {state}
        while queue:
            l = len(queue)
            for _ in range(l):
                x,y,leftK = queue.popleft()
                if (x,y) == target:
                    return length
                for d in directions:
                    nx,ny = x+d[0],y+d[1]
                    if nx>=0 and nx<m and ny>=0 and ny<n:
                        cell = grid[nx][ny]
                        if cell==0:
                            state = (nx,ny,leftK)
                            if state not in visited:
                                queue.append(state)
                                visited.add(state)
                        elif cell==1 and leftK>0:
                            state = (nx,ny,leftK-1)
                            if state not in visited:
                                queue.append(state)
                                visited.add(state)
            length+=1
        return -1
                    
       
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.shortestPath(grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1),6)
    test(sol.shortestPath(grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1),-1)
    test(sol.shortestPath([[0,0],[1,0],[1,0],[1,0],[1,0],[1,0],[0,0],[0,1],[0,1],[0,1],[0,0],[1,0],[1,0],[0,0]],4),14) # 49

# Accepted
# 52/52 cases passed (76 ms)
# Your runtime beats 80.54 % of python3 submissions
# Your memory usage beats 55.46 % of python3 submissions (15.5 MB)
