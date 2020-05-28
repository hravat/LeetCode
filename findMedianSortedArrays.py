#https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float

        Algo exlplanation
        1) Both Arrays are sorted
        2) Take an element from the shorter arrays
        3) Loop through the longer arrays
        4) If the element from first array is smaller than second
        5) Pop it in 
        6) We append infinity at the end of the longer array
        7) As a result we have a single array both sorted
        8) From this we calculate the median

        """

        num_idx = 0

        if nums1 == []:

            nums2.append(float('inf'))
            nums_fin = nums2


        elif nums2 == []:

            nums1.append(float('inf'))
            nums_fin = nums1

        elif len(nums1) <= len(nums2):

            nums_fin = nums2
            nums2.append(float('inf'))

            for i, num in enumerate(nums2):

                if nums1[num_idx] <= num:

                    nums_fin.insert(i, nums1[num_idx])
                    num_idx += 1
                    if num_idx == len(nums1):
                        break
        else:

            nums_fin = nums1
            nums1.append(float('inf'))

            for i, num in enumerate(nums1):

                if nums2[num_idx] <= num:

                    nums_fin.insert(i, nums2[num_idx])
                    num_idx += 1
                    if num_idx == len(nums2):
                        break

        nums_fin = nums_fin[:-1]
        print(nums_fin)

        if len(nums_fin) % 2 != 0:
            med = float(nums_fin[(len(nums_fin) - 1) / 2])
        else:
            med = float((nums_fin[(len(nums_fin) / 2)] + nums_fin[(len(nums_fin) / 2) - 1]))
            med /= 2

        return med
