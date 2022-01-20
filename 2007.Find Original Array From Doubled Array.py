#
# @lc app=leetcode id=2007 lang=python3
#
# [2007] Find Original Array From Doubled Array
#
from typing import List
# @lc code=start
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        l = len(changed)
        r = list()
        if l&1: return r
        changed.sort()
        i,j=0,1
        while True:
            while i<l and changed[i]==-1: i+=1
            if i==l: break
            double = changed[i]*2
            j = max(j, i+1)
            while j<l and changed[j]<double: j+=1
            if j==l or changed[j]!=double: return list()
            r.append(changed[i])
            i+=1
            changed[j]=-1
        return r


# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.findOriginalArray(changed = [1,3,4,2,6,8]), [1,3,4], False)
    test(sol.findOriginalArray(changed = [6,3,0,1]), [], False)
    test(sol.findOriginalArray(changed = [1]), [], False)
    test(sol.findOriginalArray(changed = [1,2]), [1], False)
    test(sol.findOriginalArray(changed = [1,1,2,2,2,2,4,4]), [1,1,2,2], False, True)
    test(sol.findOriginalArray(changed = [0,0,0,0]), [0,0], False, True)

# Success
# Details 
# Runtime: 2170 ms, faster than 23.88% of Python3 online submissions for Find Original Array From Doubled Array.
# Memory Usage: 29.1 MB, less than 97.10% of Python3 online submissions for Find Original Array From Doubled Array.
