#https://leetcode.com/problems/add-two-numbers/
# The list will not neceasirly be of the same lenght
# Hence if one list ends and is None all further values are set to 0 
# prev_carry keeps track if the is any acrry over fro the previous record
# using mod and divide we determine the sum of 2 numbers as well if there is any current carry
# The current sum to be determined is sum of both numbers from list as well as previous carry
# Finally using all these numbers the linked list is formed.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        arr=[]
        carry=0
        rem=0
        
        result = ListNode(0)
        result_tail = result
        
        v1=0
        v2=0
       
        
        while l1 or l2:
            
            if l1 is None:
                v1=0
            else: 
                v1=l1.val
            
            if l2 is None:
                v2=0
            else: 
                v2=l2.val
            
            prev_carry=carry
            rem=  (v1+v2+prev_carry)%10
            carry=(v1+v2+prev_carry)/10
            
            result_tail.next = ListNode(rem)
            result_tail = result_tail.next 
            
            
            if l1:
                l1 = l1.next
            else: 
                None
            
            
            if l2:
                l2 = l2.next
            else: 
                None
                
           
        
        if carry == 1:
            result_tail.next = ListNode(carry)
            result_tail = result_tail.next 
        
        result=result.next

            
        return result
        
        
        
