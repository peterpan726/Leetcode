#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = 0
        l = []
        for index, i in enumerate(digits):
            ans += i * (10 ** (len(digits) - (index + 1)))
        ans += 1
        for i in str(ans):
            l.append(i)
        return l
                 
# @lc code=end

