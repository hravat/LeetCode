## https://leetcode.com/problems/reverse-integer/

## convert int to string after removing negative sign
## append string from reverese to new string : Line 1
## convert list to string
## convert string back to int and multiply by -1 if ncesseary
## check for overflow


class Solution:
    def reverse(self, x: int) -> int:
        
        if x >= 2**31-1 or x <= -2**31:
            print(x)
            rev_int=0
        
        else :
            str_x=str(abs(x))
            print(str_x)
        
            str_list =[]
            str_rev=""
            rev_int=0
        
            for i in range(len(str_x)):
                if i > 0:
                    str_list.append(str_x[-i]) #Line 1
        
            str_list.append(str_x[0])
        
            for i in str_list:
                str_rev=str_rev+i
            
            
            rev_int=int(str_rev)
        
            if x < 0:
                rev_int=rev_int*-1
            
           
        
        
        if rev_int >= 2**31-1 or rev_int <= -2**31:
            rev_int=0
        
        return rev_int
        
            
            
            
