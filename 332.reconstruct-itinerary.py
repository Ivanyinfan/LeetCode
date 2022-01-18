#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#
from typing import List
# @lc code=start
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])
        for neigh in graph.values():
            neigh.sort(reverse=True)
        result = list()
        path = ["JFK"]
        neigh_list = [graph["JFK"]]
        while path:
            neigh = neigh_list[-1]
            if neigh:
                next = neigh.pop()
                path.append(next)
                neigh_list.append(graph[next])
            else:
                neigh_list.pop()
                result.append(path.pop())
        return list(reversed(result))
   
# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    # print(sol.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
    print(sol.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))

# 80 / 80 test cases passed.
# Status: Accepted
# Runtime: 76 ms
# Memory Usage: 14.5 MB
# Your runtime beats 89.89 % of python3 submissions.
# Your memory usage beats 95.50 % of python3 submissions.
