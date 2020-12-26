#https://leetcode.com/problems/integer-to-roman/
#Challenge 12 

 class Solution:
    def intToRoman(self, num: int) -> str:
        
        num_list = [i for i in reversed(str(num))]
        
        roman_num = ''
        
        dict_0 = {0:'',
                  1:'I',
                  2:'II',
                  3:'III',
                  4:'IV',
                  5:'V',
                  6:'VI',
                  7:'VII',
                  8: 'VIII',
                  9: 'IX'
                 }
        
        
        dict_1 = {0:'',
                  1:'X',
                  2:'XX',
                  3:'XXX',
                  4:'XL',
                  5:'L',
                  6:'LX',
                  7:'LXX',
                  8:'LXXX',
                  9:'XC'
                 }
        
        dict_2 = {0:'',
                  1:'C',
                  2:'CC',
                  3:'CCC',
                  4:'CD',
                  5:'D',
                  6:'DC',
                  7:'DCC',
                  8:'DCCC',
                  9:'CM'
                 }
        
        dict_3 = {0:'',
                  1:'M',
                  2:'MM',
                  3:'MMM'
                 }
        
        for i,num in enumerate(num_list):
            if i == 0:
                roman_num=dict_0[int(num)]+roman_num
            elif i==1:
                roman_num=dict_1[int(num)]+roman_num
            elif i==2:    
                roman_num=dict_2[int(num)]+roman_num
            else:     
                roman_num=dict_3[int(num)]+roman_num
                
                
        return roman_num        
