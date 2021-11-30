#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
from typing import List
from collections import defaultdict, deque
# @lc code=start
class Node:
    def __init__(self, word, intermediate) -> None:
        self.word = word
        self.intermediate = intermediate
        self.level = 1

    def __hash__(self) -> int:
        return hash(self.word)
    
    def __eq__(self, __o: object) -> bool:
        return self.word==__o.word

class Solution:
    def addToGraph(self, word, graph):
        wordNode = Node(word, False)
        neigh = graph[wordNode]
        for i in range(len(word)):
            tmp = Node(f'{word[:i]}*{word[i+1:]}', True)
            neigh.append(tmp)
            graph[tmp].append(wordNode)
        return wordNode

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        for word in wordList:
            self.addToGraph(word, graph)
        beginWord:Node = Node(beginWord, False)
        if beginWord not in graph:
            self.addToGraph(beginWord.word, graph)
        visited = {beginWord}
        stack = deque([beginWord])
        while stack:
            node:Node = stack.popleft()
            if not node.intermediate and node.word==endWord:
                return node.level//2+1
            for neigh in graph[node]:
                if neigh not in visited:
                    neigh.level = node.level + 1
                    stack.append(neigh)
                    visited.add(neigh)
        return 0

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]), 5)
    test(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]), 0)
    test(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog", 'hit']), 5)
    test(sol.ladderLength("hit", "cog", ["cog"]), 0)
    test(sol.ladderLength("hit", "cog", ["cog", 'hit']), 0)
    test(sol.ladderLength("hit", "cog", []), 0)

# Accepted
# 49/49 cases passed (256 ms)
# Your runtime beats 53.43 % of python3 submissions
# Your memory usage beats 5.21 % of python3 submissions (25.7 MB)
