class Solution:
    def romanToInt(self, s: str) -> int:
        
        rom_dict = {}
        rom_dict['I']=1
        rom_dict['V']=5
        rom_dict['X']=10
        rom_dict['L']=50
        rom_dict['C']=100
        rom_dict['D']=500
        rom_dict['M']=1000
        rom_dict['IV']=4
        rom_dict['IX']=9
        rom_dict['XL']=40
        rom_dict['XC']=90
        rom_dict['CD']=400
        rom_dict['CM']=900
        
        rev_s = "".join(reversed(s))
        
        dig_prev = rev_s[0]
        num = int(rom_dict[dig_prev])
        
        
        
        for dig in rev_s[1:]:
            if rom_dict[dig] < rom_dict[dig_prev]:
                num -= int(rom_dict[dig])
            else:                
                num += int(rom_dict[dig])
            dig_prev=dig
            
        
        return num