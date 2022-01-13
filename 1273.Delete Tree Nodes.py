#
# @lc app=leetcode id=1273 lang=python3
#
# [1273] Delete Tree Nodes
#
from typing import List
# @lc code=start
class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        childNum = [1]*nodes
        leftChild = [0]*nodes
        leaves = list()
        for i in range(1, nodes):
            leftChild[parent[i]]+=1
        for i in range(1, nodes):
            if leftChild[i]==0:
                leaves.append(i)
        remain = nodes
        while leaves:
            newLeaves = list()
            for leaf in leaves:
                if value[leaf]==0:
                    remain -= childNum[leaf]
                else:
                    value[parent[leaf]]+=value[leaf]
                    childNum[parent[leaf]]+=childNum[leaf]
                if parent[leaf]!=-1:
                    leftChild[parent[leaf]]-=1
                    if leftChild[parent[leaf]]==0:
                        newLeaves.append(parent[leaf])
            leaves = newLeaves
        if value[0]==0:
            return 0
        return remain
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.deleteTreeNodes(nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]),2)
    test(sol.deleteTreeNodes(nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-2]),6)
    test(sol.deleteTreeNodes(7,[-1,6,6,5,6,0,0],[1,-1,-1,0,-2,-2,4]), 2) # 20
    test(sol.deleteTreeNodes(1,[-1],[0]), 0) # 21
    test(sol.deleteTreeNodes(1,[-1],[1]), 1)

# Success 
# Runtime: 228 ms, faster than 98.08% of Python3 online submissions for Delete Tree Nodes.
# Memory Usage: 16 MB, less than 98.08% of Python3 online submissions for Delete Tree Nodes.
