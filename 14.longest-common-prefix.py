#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return " "
        if len(strs) == 1: return strs[0]

        ans = ""
        
      
# @lc code=end