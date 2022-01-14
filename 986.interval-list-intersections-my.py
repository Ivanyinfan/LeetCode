#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#
from typing import List
# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = list()
        l1,l2 = len(firstList),len(secondList)
        i=j=0
        while i<l1 and j<l2:
            if firstList[i][1]<secondList[j][0]:
                i += 1
            elif firstList[i][0]>secondList[j][1]:
                j += 1
            elif firstList[i][0]<=secondList[j][0] and firstList[i][1]>=secondList[j][1]:
                result.append(secondList[j])
                firstList[i][0]=secondList[j][1]
                j += 1
            elif firstList[i][0]>=secondList[j][0] and firstList[i][1]<=secondList[j][1]:
                result.append(firstList[i])
                secondList[j][0]=firstList[i][1]
                i += 1
            else:
                if firstList[i][0]<secondList[j][0]:
                    result.append([secondList[j][0], firstList[i][1]])
                    secondList[j][0] = firstList[i][1]
                    i += 1
                else:
                    result.append([firstList[i][0], secondList[j][1]])
                    firstList[i][0] = secondList[j][1]
                    j += 1
        return result
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]),[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]])
    test(sol.intervalIntersection(firstList = [[1,3],[5,9]], secondList = []),[])
    test(sol.intervalIntersection(firstList = [[1,1]], secondList = [[0,1]]),[[1,1]])
    test(sol.intervalIntersection(firstList = [[1,1]], secondList = [[0,0]]),[])
    test(sol.intervalIntersection(firstList = [[1,1]], secondList = [[1,2]]),[[1,1]])
    test(sol.intervalIntersection(firstList = [[1,1]], secondList = [[1,1]]),[[1,1]])

# Accepted
# 85/85 cases passed (264 ms)
# Your runtime beats 13.85 % of python3 submissions
# Your memory usage beats 61.64 % of python3 submissions (15 MB)
