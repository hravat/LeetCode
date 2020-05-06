#https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 1)Loop through string and build up current string
# 2) If character is present in current string reset current string to string excluding found character + current character
# 3) Every step take lenght of string if greater than current length reset

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        max_length=0
        curr_string = ""
        
        for i,char in enumerate(s):
            
            
            
            if char in curr_string:
                curr_string=curr_string[curr_string.index(char)+1:]+char
                
                if len(curr_string) > max_length:
                    max_length=len(curr_string)
            
            else:
                curr_string=curr_string+char
                
                if len(curr_string) > max_length:
                    max_length=len(curr_string)
                
                
            
        return max_length    
            
