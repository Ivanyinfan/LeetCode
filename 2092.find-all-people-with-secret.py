#
# @lc app=leetcode id=2092 lang=python3
#
# [2092] Find All People With Secret
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        known_set = {0, firstPerson}
        meetings.sort(key=lambda x: x[2])
        start = 0
        L = len(meetings)
        while start < L:
            end = start + 1
            while end<L and meetings[end][2]==meetings[start][2]:
                end += 1
            graph = defaultdict(list)
            stack = list()
            for i in range(start, end):
                meeting = meetings[i]
                if meeting[0] in known_set:
                    stack.append(meeting[0])
                if meeting[1] in known_set:
                    stack.append(meeting[1])
                graph[meeting[0]].append(meeting[1])
                graph[meeting[1]].append(meeting[0])
            while stack:
                node = stack.pop()
                neighbours = graph[node]
                for neighbour in neighbours:
                    known_set.add(neighbour)
                    if neighbour in graph:
                        stack.append(neighbour)
                graph.pop(node)
            start = end
        return list(known_set)
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.findAllPeople(n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1), [0,1,2,3,5], False)
    test(sol.findAllPeople(n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3), [0,1,3], False)
    test(sol.findAllPeople(n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1), [0,1,2,3,4], False)
    test(sol.findAllPeople(n = 1, meetings = [[0,1,1]], firstPerson = 1), [0,1], False)
    test(sol.findAllPeople(n = 1, meetings = [[0,1,1]], firstPerson = 0), [0,1], False)
    test(sol.findAllPeople(n = 6, meetings = [[0,2,1],[1,3,1],[4,5,1]], firstPerson = 1), [0,1,2,3], False) # 34

# Accepted
# 60/60 cases passed (2220 ms)
# Your runtime beats 79.92 % of python3 submissions
# Your memory usage beats 57.24 % of python3 submissions (52.1 MB)
