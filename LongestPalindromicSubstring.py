
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        ### We break the problen in two parts 1 where the palindromw consists of odd and 
        ### the second where it consists of even number of letters
        pal_str_odd_final =''
        pal_str_even_final =''
        pal_str= ''
        
        
        
        for i in range(len(s)):
           
            # Setting j & k for indexing
            # This will set it to before and after
            # the current central letter in question
            j=i-1
            k=i+1
            
            pal_str = s[i]
           
            #Keep expanding the string till we reach end or start of the string 
            
            while j >= 0 and k < len(s):
                
                #If letters at j & k are same 
                # add it to string else break loop
                # and move on to next letter    
                
                if s[j] == s[k]:
                    pal_str = s[j]+pal_str+s[k]
                    
                    #Set largest string as final
                    
                    if len(pal_str) > len(pal_str_odd_final):
                        pal_str_odd_final=pal_str
                        
                    
                    j -= 1
                    k += 1
                
                else:
                    break
                    
        if len(pal_str_odd_final) < len(pal_str):
            pal_str_odd_final = pal_str
        
        
        # For Even the same logic is applied
        # The only difference is that 
        # two letters are picked at a time for the centre
        # if they are same we go ahead with processing 
        # else we break loop 
        
        for i in range(len(s)-1):
            
            if s[i]==s[i+1]:
                pal_str = s[i:i+2]   
                
            else:
                continue
            
            j=i-1
            k=i+2
            
            
            while j >= 0 and k < len(s):
                    if s[j] == s[k]:
                        pal_str = s[j]+pal_str+s[k]
                    
                        if len(pal_str_even_final) < len(pal_str):
                            pal_str_even_final=pal_str
                            
                        j -= 1
                        k += 1    
                    
                    else:
                        break
        
        if len(pal_str_even_final) < len(pal_str):
            pal_str_even_final = pal_str
        
        
        if len(pal_str_even_final) > len(pal_str_odd_final):
            return pal_str_even_final
        else:
            return pal_str_odd_final
