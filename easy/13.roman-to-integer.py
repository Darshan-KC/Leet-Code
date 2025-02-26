#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        sum = pre_val = self.value(s[0])
        for i in range(1,len(s)):
            current_val = self.value(s[i])
            if(pre_val < current_val):
                sum = sum - pre_val + current_val - pre_val
            else:
                sum += current_val
                
            pre_val= current_val
        
        return sum
        
    def value(self, letter: str) -> int:
        match letter:
            case 'I':
                return 1
            case 'V':
                return 5
            case 'X':
                return 10
            case 'L':
                return 50
            case 'C':
                return 100
            case 'D':
                return 500
            case 'M':
                return 1000
            case _:
                print("Invalid value")
                exit(1)

# test = Solution()
# print(test.romanToInt("III"))
        
# @lc code=end

