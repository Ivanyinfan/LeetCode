#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
from typing import List
from collections import deque
# @lc code=start
class Node:
    def __init__(self, word, visited) -> None:
        self.word = word
        self.visited = visited
        self.level = 1
        self.father = list()
    
    def __hash__(self) -> int:
        return hash(self.word)
    
    def __eq__(self, __o: object) -> bool:
        return self.word == __o.word

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.wordDict:set = set(wordList)
        self.wordDict.discard(beginWord)
        visited = {beginWord:[1, None]}
        queue = deque([beginWord])
        while queue and endWord not in visited:
            n = len(queue)
            for i in range(n):
                word = queue.popleft()
                wordInfo = visited[word]
                neighbours = self.getNeighbours(word)
                for neighbour in neighbours:
                    if neighbour not in visited:
                        visited[neighbours] = [wordInfo[0]+1, [word]]
                        queue.append(neighbour)
                    else:
                        if visited[neighbour][0]==wordInfo[0]+1:
                            visited[neighbour][1].append(word)
        if endWord not in visited: return list()
        r = list()
        pathSet = [[endWord]]
        while pathSet:
            path = pathSet[-1]
            lastWordInfo = visited[path[-1]]
            if lastWordInfo[1]==None:
                r.append(path)
                pathSet.pop()
            else:
                for i in range(len(lastWordInfo[1])-1):
                    pathSet.append(path+[lastWordInfo[1][i]])
                path.append(lastWordInfo[1][-1])
        return r

    def getNeighbours(self, word):
        pass

# @lc code=end

