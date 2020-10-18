class Solution:
    def maxArea(self, height: List[int]) -> int:
     # Algorithm used is two pointer approach shown in solutions
     # It has been just imlemented but not developed here
     # An explanation is given at the below link
     #https://leetcode.com/problems/container-with-most-water/solution/
     
     start_height=height[0]
     end_height=height[-1]   
     start_height_idx=0
     end_height_idx=len(height)-1
     max_area =  (min(start_height,end_height))*(end_height_idx-start_height_idx)   

    
     while start_height_idx <= end_height_idx:
            
            if start_height < end_height:
                start_height_idx += 1
                start_height=height[start_height_idx]
            else:
                end_height_idx -= 1
                end_height=height[end_height_idx]
            
            area= (min(start_height,end_height))*(end_height_idx-start_height_idx)
            max_area = max(area,max_area)
            
        
     return(max_area) 
