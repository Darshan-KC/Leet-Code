#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Solution 1
        y = str(x)
        tem = y[::-1]
        if y == tem:
            return True
        return False
    
        # Solution 2
        # if x == 0:
        #     return True
        
        # elif x % 10 == 0:
        #     return False
        
        # half = 0
        
        # while(x > half):
        #     half = half * 10 + x % 10
        #     x //=10
            
        # if x == half or half // 10 == x:
        #     return True
        
        # return False
        
        
# @lc code=end
# test = Solution()
# print(test.isPalindrome(-121))
