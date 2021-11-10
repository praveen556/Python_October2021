'''
46. Permutations
Medium

7914

157

Add to List

Share
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.


'''

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        results = []
        def helper(nums, i, slate):
            if i==len(nums):
                results.append(nums[:])
            else:
                for pick in range(i, len(nums)):
                    nums[pick], nums[i] = nums[i], nums[pick]
                    slate.append(nums[i])
                    helper(nums, i+1, slate)
                    slate.pop()
                    nums[pick], nums[i] = nums[i], nums[pick]
        helper(nums,0,[])
        return results

print(Solution.permute(1,[1,2,3]))

'''
Runtime: 36 ms, faster than 91.52% of Python3 online submissions for Permutations.
Memory Usage: 14.2 MB, less than 97.19% of Python3 online submissions for Permutations.

'''


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        results = []
        def helper(nums, i):
            if i==len(nums):
                results.append(nums[:])
            else:
                for pick in range(i, len(nums)):
                    nums[pick], nums[i] = nums[i], nums[pick]
                    helper(nums, i+1)
                    nums[pick],nums[i] = nums[i], nums[pick]
        helper(nums,0)
        return results

'''
Runtime: 40 ms, faster than 78.03% of Python3 online submissions for Permutations.
Memory Usage: 14.5 MB, less than 15.29% of Python3 online submissions for Permutations.
'''

#Solution 3 using Python internal Libraries


from itertools import permutations

def get_permutations(arr):
    output = list()
    for p in permutations(arr):
        output.append(p)
    return output
