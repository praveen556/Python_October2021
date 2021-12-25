'''

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
'''



#Solution1
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)==0 and len(nums2)==0:
            return 0
        i, j, result_list = 0, 0, []

        mid_length = (len(nums1)+ len(nums2))//2

        while i<len(nums1) or j<len(nums2):
            if i+j > mid_length:
                break

            if i <len(nums1) and j<len(nums2):

                if nums1[i]<nums2[j]:
                    result_list.append(nums1[i])
                    i+=1

                else:
                    result_list.append(nums2[j])
                    j+=1

            elif i<len(nums1):
                result_list.append(nums1[i])
                i+=1

            else:
                result_list.append(nums2[j])
                j+=1
        if (len(nums1)+ len(nums2))%2==1:
            return result_list[-1]
        else:
            return (result_list[-1]+result_list[-2])/2

'''
Runtime: 93 ms, faster than 55.87% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.6 MB, less than 56.18% of Python3 online submissions for Median of Two Sorted Arrays.
'''



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)==0 and len(nums2)==0:
            return 0
        result_list = []

        result_list = nums1 + nums2

        result_list.sort()

        if (len(result_list))%2==1:
            return result_list[len(result_list)//2]
        else:
            return (result_list[len(result_list)//2]+result_list[len(result_list)//2-1])/2

'''
Runtime: 106 ms, faster than 30.85% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.5 MB, less than 81.09% of Python3 online submissions for Median of Two Sorted Arrays.
'''
