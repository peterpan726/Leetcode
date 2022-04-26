#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        for i in s :
            if s[i] != s[i+1]:
                break
            else:
                pass
                

        
# @lc code=end

