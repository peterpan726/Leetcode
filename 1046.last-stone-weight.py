#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution:   
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            y = stones[-1]
            x = stones[-2]
            if x == y:
                stones.pop(-1)
                stones.pop(-1)
            else:
                stones.pop(-1)
                stones[-1] = y-x
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
        

# @lc code=end

