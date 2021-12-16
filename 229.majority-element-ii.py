#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
from typing import List
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1=count1=candidate2=count2=0
        for num in nums:
            if count1!=0 and num==candidate1:
                count1+=1
            elif count2!=0 and num==candidate2:
                count2+=1
            elif count1==0:
                candidate1,count1 = num, 1
            elif count2==0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        r = list()
        l = len(nums)
        l_3 = l // 3
        if count1!=0 and nums.count(candidate1)>l_3: r.append(candidate1)
        if count2!=0 and nums.count(candidate2)>l_3: r.append(candidate2)
        return r
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.majorityElement([3,2,3]),[3])
    test(sol.majorityElement([1]),[1])
    test(sol.majorityElement([1,2]),[1,2])
    test(sol.majorityElement([1,2,3]),[])
    test(sol.majorityElement([1,1,2,2,2,2,2,3]),[2])
    test(sol.majorityElement([1,1,1,2,2,2,2,3]),[1,2])

# Accepted
# 82/82 cases passed (175 ms)
# Your runtime beats 12.69 % of python3 submissions
# Your memory usage beats 31.97 % of python3 submissions (15.5 MB)
