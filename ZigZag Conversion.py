class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        str_ind_all = []
        str_ind=[0]
        str_row=[]
        str_row_diag = []
        i=1
        z=0
        str_final=''
        
        ### The entire Algo is based on the following steps 
        ### The number of rows determines the number of indices
        ### For 3 rows the first row will be [0,4,8..]
        ### For 4 Rows the first row will be [0.6.12..] and so on
        ### This can be calculated using the formula 2(numRows-1)*iteration : Formula 1
        ### Likewise diagonal elements can be calculated Formula 2
        ### Thus each row is added in a list and finally appenedd to a final list
        ### Each list os sorted an looped through to build the final string
        ### If there is one row the string is as it is
        ### We levae all indices less than 0 or greater than string length
        
        if numRows==1:
            str_final=s
        else:   
            while z < len(s):
                z = 2*(numRows-1)*i #Formula 1
                i += 1
                if z < len(s):
                    str_ind.append(z)
            
            str_ind_all.append(str_ind)    
        
        
            for i in range (1,numRows):
                str_row = [i+j for j in str_ind]
                if i != (numRows-1):
                    str_row_diag = [j+(2*(numRows-1-i)) for j in str_row] #Formula 2
                else:
                    str_row_diag=[]
                str_row.extend(str_row_diag)
                str_row.sort()
                str_ind_all.append(str_row)
            
            
            
            print(str_ind_all)
            
            for row in str_ind_all:
                for i in row:
                    if i >= 0 and i < len(s):
                        str_final=str_final+s[i]
                        
            
            
            
            
        return str_final 
