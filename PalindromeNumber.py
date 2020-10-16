#https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        is_palindrome=True
        if x == 0:
            number_of_digits=1
        else:    
            ## This helps compute the number of digits in a number
            number_of_digits = int(math.log10(abs(x)))+1
        
        
        
        if x < 0:
            is_palindrome = False
        else:
            for i in range(0,number_of_digits):
                #This code gets the digit if i = 0 we get first digit 1 second digit and so on
                #In a single pass we pick first and last and so on 
                # We compare them if equal continue else break an retiyrn false
                num_back = (x // 10**i % 10)
                num_front =(x // 10**(number_of_digits-i-1) % 10)
                if num_back != num_front:
                    is_palindrome = False
                    break
                
        return is_palindrome   
