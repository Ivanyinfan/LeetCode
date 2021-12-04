#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    ord_a = ord('a')
    ord_z = ord('z')

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
                        visited[neighbour] = [wordInfo[0]+1, [word]]
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
        for path in r: path.reverse()
        return r

    def getNeighbours(self, word) -> list[str]:
        char_list = list(word)
        result = list()
        for i, char in enumerate(char_list):
            for j in range(Solution.ord_a, Solution.ord_z+1):
                new_char = chr(j)
                if new_char != char:
                    char_list[i]=new_char
                    new_word = ''.join(char_list)
                    if new_word in self.wordDict:
                        result.append(new_word)
            char_list[i]=char
        return result

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]), [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]])
    test(sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log"]), [])
    test(sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog", 'hit']), [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]])
    test(sol.findLadders("hit", "cog", ["cog"]), [])
    test(sol.findLadders("hit", "cog", ["cog", 'hit']), [])
    test(sol.findLadders("hit", "cog", []), [])

# Accepted
# 32/32 cases passed (52 ms)
# Your runtime beats 74.85 % of python3 submissions
# Your memory usage beats 74.71 % of python3 submissions (14.7 MB)
