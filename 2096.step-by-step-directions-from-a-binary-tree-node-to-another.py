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
        
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        fathers = dict()
        pathResult = [None]*2
        self.startValue = startValue
        self.destValue = destValue
        self.dfs(root, list(), fathers, pathResult)
        l1,l2 = len(pathResult[0]), len(pathResult[1])
        path2_set = set(pathResult[1])
        result = list()
        LCA = None
        for i in range(l1-1, -1, -1):
            if pathResult[0][i] not in path2_set:
                result.append('U')
            else:
                LCA = pathResult[0][i]
                break
        index = pathResult[1].find(LCA)
        currNode = LCA
        while currNode.val!=destValue:
            if pathResult[1][index+1]==currNode.left:
                result.append('L')
            else:
                result.append('R')
        return ''.join(result)
        
# @lc code=end  

