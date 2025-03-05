#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    def longestCommonPrefix(self, strs) -> str:
        result = ""
        count = 0
        l = len(strs)
        index = 0
        counter = 0
        
        while True:
            print("while")
            
            temp = self.compareString(strs[count], result)
            
            if (temp == 0):
                if(counter == 2):
                    result = strs[0][index]
                    index += 1
                counter +=1
                print("if")
                
            elif (temp == 1):
                if counter == 2:
                    result += strs[0][index]
                    index += 1
                counter +=1
                print("elif")
            
            elif (temp == -1):
                break
                
            if(count == l-1):
                count = counter = 0
                
            count += 1
            print(f'before end count => {count} and temp => {temp} and counter => {counter}')
        return result
            
    
    def compareString(self, string, comp_str) -> bool:
        if comp_str == "":
            return 0
        elif string.startswith(comp_str):
            return 1
        else:
            return -1
        
        
# @lc code=end

soln = Solution()
result = soln.longestCommonPrefix(["flower","flow","flight"]
)
print(result)