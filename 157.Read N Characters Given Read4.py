#
# @lc app=leetcode id=157 lang=python3
#
# [157] Read N Characters Given Read4
#

# @lc code=start
"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        i = 0
        buf4 = [None]*4
        while i<n:
            m = read4(buf4)
            if m==0:
                break
            j = 0
            while i<n and j<m:
                buf[i]=buf4[j]
                i, j = i+1, j+1
        return i
        
# @lc code=end

# Success
# Details 
# Runtime: 45 ms, faster than 24.66% of Python3 online submissions for Read N Characters Given Read4.
# Memory Usage: 14.2 MB, less than 57.97% of Python3 online submissions for Read N Characters Given Read4.
