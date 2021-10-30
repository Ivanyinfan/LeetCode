#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
from typing import List
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2): nums1,nums2= nums2, nums1
        if len(nums1)==0: return (nums2[(len(nums2)-1)//2]+nums2[len(nums2)//2])/2
        L = len(nums1)+len(nums2)
        k,s1,s2= L//2,0,0
        while k>1 and s1<len(nums1) and s2<len(nums2):
            os1,os2 = s1,s2
            nk = k//2
            c1,c2 = min(len(nums1)-1,s1+nk-1), min(len(nums2)-1,s2+nk-1)
            if nums1[c1]<nums2[c2]: s1=c1+1
            else: s2 = c2+1
            k -= s1-os1+s2-os2
        if s1==len(nums1):
            if L%2: return nums2[s2+k]
            return (nums2[s2+k-1]+nums2[s2+k])/2
        if s2==len(nums2):
            if L%2: return nums1[s1+k]
            return (nums1[s1+k-1]+nums1[s1+k])/2
        if L%2:
            if nums1[s1]<nums2[s2]:
                if s1+1<len(nums1): return min(nums1[s1+1], nums2[s2])
                return nums2[s2]
            if s2+1<len(nums2): return min(nums1[s1], nums2[s2+1])
            return nums1[s1]
        if nums1[s1]<nums2[s2]:
            if s1+1<len(nums1): return (nums1[s1]+min(nums1[s1+1], nums2[s2]))/2
            return (nums1[s1]+nums2[s2])/2
        if s2+1<len(nums2): return (nums2[s2]+min(nums1[s1], nums2[s2+1]))/2
        return (nums1[s1]+nums2[s2])/2
            

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.findMedianSortedArrays([1,3],[2]),2)
    test(sol.findMedianSortedArrays([1,2],[3,4]),2.5)
    test(sol.findMedianSortedArrays([0,0],[0,0]),0)
    test(sol.findMedianSortedArrays([],[1]),1)
    test(sol.findMedianSortedArrays([2],[]),2)
    test(sol.findMedianSortedArrays([2,3],[]),2.5)
    test(sol.findMedianSortedArrays([2,3,4],[]),3)
    test(sol.findMedianSortedArrays([3],[-2,-1]),-1)    #48
    test(sol.findMedianSortedArrays([1,2],[-1,3]),1.5)  #51
    test(sol.findMedianSortedArrays([1],[2,3,4]),2.5)   #54

# Accepted
# 2094/2094 cases passed (88 ms)
# Your runtime beats 89.74 % of python3 submissions
# Your memory usage beats 54.92 % of python3 submissions (14.6 MB)
