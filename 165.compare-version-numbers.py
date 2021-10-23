#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#
from utils import test
# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1,v2=[int(num) for num in version1.split('.')],[int(num) for num in version2.split('.')]
        lt,gt,eq=-1,1,0
        if len(v1)>len(v2): v1,v2,lt,gt=v2,v1,1,-1
        for i,v in enumerate(v1):
            if v<v2[i]: return lt
            if v>v2[i]: return gt
        for i in range(len(v1),len(v2)):
            if v2[i]>0: return lt
        return eq
            
# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    test(sol.compareVersion("1.01","1.001"),0)
    test(sol.compareVersion("1.0","1.0.0"),0)
    test(sol.compareVersion("0.1","1.1"),-1)
    test(sol.compareVersion("1.0.1","1"),1)
    test(sol.compareVersion("7.5.2.4","7.5.3"),-1)

# Accepted
# 81/81 cases passed (52 ms)
# Your runtime beats 13.46 % of python3 submissions
# Your memory usage beats 58.4 % of python3 submissions (14.2 MB)
