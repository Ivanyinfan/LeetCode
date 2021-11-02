from typing import List
from collections import defaultdict
class Solution:
    def solution(self, A:List[int]) -> int:
        sum_map = defaultdict(set)
        for i, num in enumerate(A):
            for j in range(i+1, len(A)):
                summ = num+A[j]
                if i in sum_map[summ] or j in sum_map[summ]: continue
                sum_map[summ].add(i)
                sum_map[summ].add(j)
        return max(map(lambda x:len(x), sum_map.values()))//2

from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.solution([1,9,8,100,2]),2)
    test(sol.solution([2,2,2,3]),1)
    test(sol.solution([5,5]),1)
    test(sol.solution([2,2]),1)
    test(sol.solution([2,2,2]),1)
    test(sol.solution([2,2,2,2]),2)
    test(sol.solution([2,2,2,2,2]),2)
    test(sol.solution([2,2,2,2,2,1,3]),3)
    test(sol.solution([2,2,2,2,2,1,1,3]),3)
