#https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        num_list=[]
        
        for i in range(len(nums)-2):
            left_pointer=i+1
            right_pointer=len(nums)-1
            curr_sum = nums[i]+nums[left_pointer]+nums[right_pointer]
            
            while left_pointer <= right_pointer:
                curr_sum = nums[i]+nums[left_pointer]+nums[right_pointer] 
                if curr_sum < 0:
                    left_pointer=left_pointer+1   
                elif curr_sum > 0: 
                    right_pointer=right_pointer-1
                else:
                    if i != left_pointer and i !=right_pointer and left_pointer!=right_pointer:
                        if [nums[i],nums[left_pointer],nums[right_pointer]] not in num_list:
                            num_list.append([nums[i],nums[left_pointer],nums[right_pointer]])
                    left_pointer=left_pointer+1
                 

        return num_list
            