#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = []
        for i in nums:
            sum.append(i + (i+1))

# @lc code=end

