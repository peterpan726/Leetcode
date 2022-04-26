#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        tmp = [None]
        dic = {'(':')', '[':']', '{':'}'}
        for i in s :
            if i in dic :
                if dic[i] != tmp.pop():
                    return False
            else:
                tmp.append(i)
        return len(tmp) == 1
        
# @lc code=end

