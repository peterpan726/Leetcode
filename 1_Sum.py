from typing import List
from unicodedata import name

#------My first logic-----#
# Space: O(1), Time O(n^2)
def twoSum(nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i< j:
                    if nums[i] + nums[j] == target:
                        return [i, j]
                
#-----Fix my logic-----#
# Space: O(1), Time: O(n^2)
def twoSum1(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j] 

#------Another logic-----#
# Space: O(n), Time: O(n)
def twoSum2(nums: List[int], target: int) -> List[int]:
    dict = {}
    for i, v in enumerate(nums):
        if target - v in dict:
            return [dict[target - v], i]
        else:
            dict[v] = i


if __name__ == '__main__':
    a = twoSum2([3, 2, 4], 6)
    print(a)
    
    
