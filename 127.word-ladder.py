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

class Solution:
    def addToGraph(self, word, graph):
        wordNode = Node(word, False)
        for i in range(len(word)):
            tmp = Node(f'{word[:i]}*{word[i+1:]}', True)
            graph[wordNode].append(tmp)
            graph[tmp].append(word)

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        for word in wordList:
            self.addToGraph(word, graph)
        if endWord not in graph:
            return 0
        if beginWord not in graph:
            self.addToGraph(beginWord, graph)
        visited = {beginWord}
        stack = deque()
        while stack:
            node:Node = stack.popleft()


# @lc code=end

