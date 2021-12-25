'''Given an integer array nums, find three numbers whose product is maximum and return the maximum product.



Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6


Constraints:

3 <= nums.length <= 104
-1000 <= nums[i] <= 1000
'''

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])


  '''
Runtime: 244 ms, faster than 93.49% of Python3 online submissions for Maximum Product of Three Numbers.
Memory Usage: 15.5 MB, less than 46.34% of Python3 online submissions for Maximum Product of Three Numbers.

  '''
