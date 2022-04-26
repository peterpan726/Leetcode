#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start


class Solution:
    def reverse(self, x: int) -> int:
        mi = '-'
        sx = str(x)
        sy = str(abs(x))
        if x < 0:
            st = int(''.join(mi + sy[::-1]))
        else:
            st = int(''.join(sx[::-1]))

        if  st <= -(2 ** 31) or st >= (2 ** 31) - 1 :
            st = 0

        return st 
            

        

# @lc code=end

