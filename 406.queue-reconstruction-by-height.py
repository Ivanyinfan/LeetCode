#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#
from typing import List
# @lc code=start
class MyList(list):
    def __lt__(self, __x: list[int]) -> bool:
        if self[0]==__x[0]:
            return self[1]>=__x[1]
        return self[0]<__x[0]

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        for i, p in enumerate(people): people[i]=MyList(p)
        people.sort(reverse=True)
        result = list()
        for p in people:
            result.insert(p[1],p)
        return result
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    Output = [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
    test(sol.reconstructQueue(people),Output)
    people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
    Output = [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
    test(sol.reconstructQueue(people),Output)
    people = [[6,0],[5,0]]
    Output = [[5,0],[6,0]]
    test(sol.reconstructQueue(people),Output)
    people = [[6,0],[5,1]]
    Output = [[6,0],[5,1]]
    test(sol.reconstructQueue(people),Output)
    people = [[1,0]]
    Output = [[1,0]]
    test(sol.reconstructQueue(people),Output)

# Accepted
# 36/36 cases passed (108 ms)
# Your runtime beats 42.81 % of python3 submissions
# Your memory usage beats 86.41 % of python3 submissions (14.8 MB)
