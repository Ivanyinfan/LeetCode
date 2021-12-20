#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
from typing import List
# @lc code=start
class Node:
    def __init__(self, word=None, mapp=None, parent=None, parentKey=None) -> None:
        self.word = word
        self.map = mapp
        self.parent = parent
        self.parentKey = parentKey

class Trie:
    def __init__(self) -> None:
        self.root = Node(mapp=dict())
    
    def insert(self, word:str):
        node = self.root
        for char in word:
            if char not in node.map:
                newNode = Node(None, dict(), node, char)
                node.map[char] = newNode
            node = node.map[char]
        node.word = word

class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
        result = list()
        node = trie.root
        for i in range(m):
            for j in range(n):
                if board[i][j] in node.map:
                    self.backtrack(board, i, j, node.map[board[i][j]], result)
        return result

    def backtrack(self, board, i, j, node, result):
        if node.word!=None:
            result.append(node.word)
            curr:Node = node
            curr.word = None
            while curr.word==None and len(curr.map)==0 and curr.parent!=None:
                parent, parentKey = curr.parent, curr.parentKey
                parent.map.pop(parentKey)
                curr = parent
        char = board[i][j]
        board[i][j]='.'
        if i!=0:
            nextChar = board[i-1][j]
            if nextChar!='.' and nextChar in node.map:
                self.backtrack(board,i-1,j,node.map[nextChar],result)
        if i!=len(board)-1:
            nextChar = board[i+1][j]
            if nextChar!='.' and nextChar in node.map:
                self.backtrack(board,i+1,j,node.map[nextChar],result)
        if j!=0:
            nextChar = board[i][j-1]
            if nextChar!='.' and nextChar in node.map:
                self.backtrack(board,i,j-1,node.map[nextChar],result)
        if j!=len(board[0])-1:
            nextChar = board[i][j+1]
            if nextChar!='.' and nextChar in node.map:
                self.backtrack(board,i,j+1,node.map[nextChar],result)
        board[i][j]=char
            

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]),["eat","oath"],False)
    test(sol.findWords(board = [["a","b"],["c","d"]], words = ["abcb"]),[],False)
    test(sol.findWords(board = [["a"]], words = ["a","b"]),["a"],False)
    test(sol.findWords(board = [["a"]], words = ["a"]),["a"],False) # 3

# Accepted
# 62/62 cases passed (236 ms)
# Your runtime beats 99.75 % of python3 submissions
# Your memory usage beats 19.42 % of python3 submissions (16.5 MB)
