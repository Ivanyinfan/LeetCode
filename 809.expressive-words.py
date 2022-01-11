#
# @lc app=leetcode id=809 lang=python3
#
# [809] Expressive Words
#
from typing import List
# @lc code=start
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        L = len(s)
        character = [[s[0],1]]
        for i in range(1, L):
            if s[i]==s[i-1]:
                character[-1][1]+=1
            else:
                character.append([s[i],1])
        character_len = len(character)
        result = 0
        for word in words:
            l = len(word)
            i=j=0
            while i<character_len and j<l:
                if word[j]!=character[i][0]:
                    break
                end = j+1
                while end<l and word[end]==word[j]:
                    end += 1
                cnt = end - j
                if character[i][1]<3 and cnt!=character[i][1]:
                    break
                if character[i][1]>=3 and cnt>character[i][1]:
                    break
                i+=1
                j = end
            if i==character_len and j==l:
                result+=1
        return result

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.expressiveWords(s = "heeellooo", words = ["hello", "hi", "helo"]),1)
    test(sol.expressiveWords(s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]),3)
    test(sol.expressiveWords(s = "a", words = ["a"]),1)
    test(sol.expressiveWords(s = "a", words = ["aa"]),0)
    test(sol.expressiveWords(s = "aa", words = ["a"]),0)
    test(sol.expressiveWords(s = "aaa", words = ["a"]),1)

# Accepted
# 34/34 cases passed (48 ms)
# Your runtime beats 83.13 % of python3 submissions
# Your memory usage beats 96.63 % of python3 submissions (14.2 MB)
