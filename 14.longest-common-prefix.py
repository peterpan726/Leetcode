#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs: return " " # if not 可以用來檢查資料及是否為空

        for i,c in enumerate(zip(*strs)): # *類似zip的用法
            if len(set(c)) > 1 :
                return strs[0][:i]
        return min(strs)
        
# @lc code=end

