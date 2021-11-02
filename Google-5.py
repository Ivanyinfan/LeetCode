from typing import List
class Solution:
    def solution(self, A:List[int]) -> int:
        plus_map,minus_map,k = dict(),dict(),0
        for i, num in enumerate(A):
            plus,minus = num+i, num-i
            if plus in plus_map: k=max(k,i-plus_map[plus])
            else: plus_map[plus]=i
            if minus in minus_map: k=max(k,i-minus_map[minus])
            else: minus_map[minus]=i
        return k

from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.solution([2,2,2,1]),1)
    test(sol.solution([2,4,6,7,4,7,2]),5)
    test(sol.solution([100,100,100]),0)
    test(sol.solution([100000]),0)
    test(sol.solution([1,1]),0)
    test(sol.solution([1,2]),1)
    test(sol.solution([2,1]),1)
    test(sol.solution([2,1,88]),1)
    test(sol.solution([0,1,2,3,4,5,6]),6)
    test(sol.solution([0,1,2,3,-4,-5,-6]),6)
    
