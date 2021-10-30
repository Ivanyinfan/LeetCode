class Solution:
    def solution(self, s:str) -> str:
        pos_map = dict()
        for i, char in enumerate(s): pos_map[char]=i
        max_len, start, end = 1,0,0
        for i, char in enumerate(s):
            lenn = pos_map[char]-i+1
            if lenn>max_len:
                max_len, start, end = lenn, i, pos_map[char]
        return s[start:end+1]
    
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.solution('cbaabaab'),'baabaab')
    test(sol.solution('performance'),'erformance')
    test(sol.solution('cat'),'c')
