#https://leetcode.com/problems/string-to-integer-atoi/submissions/
#https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, str: str) -> int:


       str=str.strip()+" "
       first_char = str[0]
       str_int=''   

       if first_char.isdigit() or first_char=='-' or first_char=='+':
             if first_char=='-' or first_char=='+':
                    start_position=1
             else:       
                    start_position=0
             for i in range(start_position,len(str)):
                char=str[i]
                if char.isdigit():
                    str_int=str_int+char
                else:
                    break
       else:
            str_int=0

       if str_int=='':
        str_int=0

       str_int=int(str_int)

       if first_char=='-':
            str_int=str_int*-1

       if str_int >= 2147483647 or str_int <= -2147483648:
           if first_char=='-':
               str_int=-2147483648
           else:
            str_int=2147483647

       return str_int    
