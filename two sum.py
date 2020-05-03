# https://leetcode.com/problems/two-sum/submissions/
# Managed to implement in one pass
# loop throught the list
# Build a dictionary with element a key and (complement,index) as value
# For every element check if complement exits
# If yes pull out the index if no continues

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dict_targ = {}
        l_index=[]
        
        for i in range(len(nums)):
                
                diff = target-nums[i]
                
                if (diff) in dict_targ:
                    a=dict_targ[diff]
                    l_index=[i,a[1]]
                    break
                
                dict_targ[nums[i]] = (target-nums[i],i)
                
                
                
                    
        l_index.sort()   
