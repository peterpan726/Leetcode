#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start



class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        r = reversed(s)
        for i, j  in zip(s, r):
            if i == j:
                pass
            else:
                return False
        return True

        
# @lc code=end

