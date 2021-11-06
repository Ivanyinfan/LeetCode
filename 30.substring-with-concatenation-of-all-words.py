#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
from typing import List
from collections import Counter, defaultdict
# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        counter = Counter(words)
        l = len(words[0])
        re = list()
        for i in range(l):
            splits = [s[j:j+l] for j in range(i, len(s)-l+1,l)]
            left, right, c, pos = 0, 0, len(counter), defaultdict(int)
            while True:
                if c:
                    if right>=len(splits): break
                    if splits[right] in counter:
                        if pos[splits[right]]<counter[splits[right]]:
                            pos[splits[right]]+=1
                            if pos[splits[right]]==counter[splits[right]]:
                                c = c - 1
                            right+=1
                        else:
                            if pos[splits[left]]==counter[splits[left]]:
                                c = c + 1
                            pos[splits[left]] -= 1
                            left = left + 1
                    else:
                        left=right=right+1
                        c, pos = len(counter), defaultdict(int)
                else:
                    re.append(i+left*l)
                    left = right = left + 1
                    c, pos = len(counter), defaultdict(int)
        return re
   
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.findSubstring("barfoothefoobarman", ["foo","bar"]), [0,9], False)
    test(sol.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]), [], False)
    test(sol.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]), [6,9,12], False)
    test(sol.findSubstring("aaaaaaaaa", ["a","a","a",'b']), [], False)
    test(sol.findSubstring("aaaaaaaaa", ["a","a","a"]), [0,1,2,3,4,5,6], False)
    test(sol.findSubstring("abab", ["ab","ab"]), [0], False)
    test(sol.findSubstring("aabab", ["ab","ab"]), [1], False)

# Accepted
# 176/176 cases passed (92 ms)
# Your runtime beats 85.25 % of python3 submissions
# Your memory usage beats 12.22 % of python3 submissions (15 MB)
