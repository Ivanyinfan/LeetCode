#
# @lc app=leetcode id=2096 lang=python3
#
# [2096] Step-By-Step Directions From a Binary Tree Node to Another
#
from os import path
from typing import Optional
from utils import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, treeNode:TreeNode, path:list, fathers:dict, pathResult:list):
        path.append(treeNode)
        if treeNode.val == self.startValue:
            pathResult[0]=path.copy()
            if all(pathResult): return
        elif treeNode.val == self.destValue:
            pathResult[1]=path.copy()
            if all(pathResult): return
        if treeNode.left:
            fathers[treeNode.left]=treeNode
            self.dfs(treeNode.left, path, fathers, pathResult)
        if treeNode.right:
            fathers[treeNode.right]=treeNode
            self.dfs(treeNode.right, path, fathers, pathResult)
        path.pop()
        
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        fathers = dict()
        pathResult = [None]*2
        self.startValue = startValue
        self.destValue = destValue
        self.dfs(root, list(), fathers, pathResult)
        l1,l2 = len(pathResult[0]), len(pathResult[1])
        # path1 = list(map(lambda x:x.val, pathResult[0]))
        # path2 = list(map(lambda x:x.val, pathResult[1]))
        path2_dict = dict()
        for i, node in enumerate(pathResult[1]):
            path2_dict[node]=i
        result = list()
        LCA = None
        for i in range(l1-1, -1, -1):
            if pathResult[0][i] not in path2_dict:
                result.append('U')
            else:
                LCA = pathResult[0][i]
                break
        index = path2_dict[LCA]+1
        while index!=l2:
            if pathResult[1][index]==pathResult[1][index-1].left:
                result.append('L')
            else:
                result.append('R')
            index+=1
        return ''.join(result)
        
# @lc code=end
from utils import test, list2TreeNode
if __name__ == "__main__":
    sol = Solution()  
    test(sol.getDirections(root = list2TreeNode([5,1,2,3,None,6,4]), startValue = 3, destValue = 6), "UURL")
    test(sol.getDirections(root = list2TreeNode([2,1]), startValue = 2, destValue = 1), "L")

# Success 
# Runtime: 1108 ms, faster than 45.71% of Python3 online submissions for Step-By-Step Directions From a Binary Tree Node to Another.
# Memory Usage: 134.8 MB, less than 57.32% of Python3 online submissions for Step-By-Step Directions From a Binary Tree Node to Another.
