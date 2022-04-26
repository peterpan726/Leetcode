#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mer = []
        for i, j in zip(list1, list2):
            if i == j:
                mer.append(i)
                mer.append(j)
            elif i < j: 
                mer.append(i)
                mer.append(j)
            else: 
                mer.append(j)
                mer.append(i)
        return mer
        
# @lc code=end

