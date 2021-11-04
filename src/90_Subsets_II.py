'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        def helper(nums, i, slate):
            if i==len(nums):
                results.append(slate[:])
            else:
                count = 1 #Number of courses
                j = i+1 #How many more are there
                while j < len(nums) and nums[i] == nums[j]:
                    #moving forward untill we get a duplicate
                    count += 1
                    j += 1
                #count stores number of duplicates
                #When you do include we have to check how many times we do include
                for copies in range(0, count+1):
                    for op in range(copies):
                        slate.append(nums[i])
                    helper(nums,i+count,slate)#Including all the variances
                    #Removing all the variances
                    for op in range(copies):
                        slate.pop()
        helper(nums,0,[])
        return results
