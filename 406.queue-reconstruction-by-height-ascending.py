#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#
from typing import List
# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ordered = people.copy()
        ordered.sort()
        pos_map = dict()
        L = len(people)
        result = [None]*L
        for i in range(L): pos_map[i]=i
        beforeCount = 0
        for i, person in enumerate(ordered):
            if i>0 and ordered[i][0]==ordered[i-1][0]: beforeCount+=1
            else: beforeCount=0
            index = person[1]-beforeCount
            pos = pos_map[index]
            result[pos] = person
            for j in range(index, L-i-1):
                pos_map[j]=pos_map[j+1]
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
# 36/36 cases passed (332 ms)
# Your runtime beats 22.87 % of python3 submissions
# Your memory usage beats 34.41 % of python3 submissions (15 MB)
