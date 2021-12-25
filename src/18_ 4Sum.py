'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''

class Solution:
    def fourSum(self, nums, target):

        nums.sort()

        results = []


        def findNsum(nums, target, N, result):

            if len(nums) < N or N < 2: return

        # solve 2-sum
            if N == 2:

                l,r = 0,len(nums)-1

                while l < r:

                    if nums[l] + nums[r] == target:

                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                        while r > l and nums[r] == nums[r + 1]:
                            r -= 1

                    elif nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(0, len(nums)-N+1):   # careful about range
                    if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                        break
                    if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]])

        findNsum(nums, target, 4, [])

        return results

'''
Runtime: 100 ms, faster than 87.47% of Python3 online submissions for 4Sum.
Memory Usage: 14.4 MB, less than 28.86% of Python3 online submissions for 4Sum.
'''
