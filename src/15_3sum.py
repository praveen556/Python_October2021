'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []

'''

#Solution 1

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length<=1:
            return []
        nums.sort()
        results = []
        for i in range(length-2):
            if nums[i] == nums[i-1] and i>0:
                continue
            j, k = i+1, length-1
            while j < k:

                if nums[j]+nums[k]+nums[i] == 0:
                    results.append([nums[i],nums[j],nums[k]])

                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
                elif nums[j]+nums[k]+nums[i] < 0 :
                    j+=1
                else:
                    k-=1
        return results

'''
Runtime: 1522 ms, faster than 38.10% of Python3 online submissions for 3Sum.
Memory Usage: 17.5 MB, less than 50.60% of Python3 online submissions for 3Sum.
'''

#Solution 2


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length<=1:
            return []
        nums.sort()
        results = []

        def twosum(i):
            j, k = i+1, len(nums)-1
            while j < k:
                temp = nums[i]+nums[j]+nums[k]

                if temp <0:
                    j += 1

                elif temp>0:
                    k -= 1

                else:
                    results.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j]==nums[j-1]:
                        j+=1

        for i in range(length):
            if nums[i]>0:
                break
            if i==0 or nums[i]!=nums[i-1]:
                twosum(i)
        return results
'''
Runtime: 643 ms, faster than 96.58% of Python3 online submissions for 3Sum.
Memory Usage: 17.5 MB, less than 50.60% of Python3 online submissions for 3Sum.

'''
