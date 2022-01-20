#
# @lc app=leetcode id=2007 lang=python3
#
# [2007] Find Original Array From Doubled Array
#
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        l = len(changed)
        r = list()
        if l&1: return r
        counter = Counter(changed)
        keys = list(counter.keys())
        keys.sort()
        if keys[0]==0:
            cnt = counter[keys[0]]
            if cnt&1: return r
            r.extend([0]*(cnt//2))
            i = 1
        else:
            i = 0
        while True:
            while i<len(keys) and keys[i] not in counter:
                i+=1
            if i==len(keys):
                break
            double = keys[i]*2
            i_cnt = counter[keys[i]]
            if double not in counter or counter[double]<i_cnt:
                return list()
            r.extend([keys[i]]*i_cnt)
            counter.pop(keys[i])
            if counter[double]==i_cnt:
                counter.pop(double)
            else:
                counter[double]-=i_cnt
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

# Success
# Details 
# Runtime: 1772 ms, faster than 39.00% of Python3 online submissions for Find Original Array From Doubled Array.
# Memory Usage: 32.2 MB, less than 78.41% of Python3 online submissions for Find Original Array From Doubled Array.
