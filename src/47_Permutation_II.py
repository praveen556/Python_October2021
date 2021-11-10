'''
47. Permutations II
Medium

3881

86

Add to List

Share
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results


# Solution 2 Based on InterviewKickStart


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def helper(nums, i):
            if len(nums)==i:
                results.append(nums[:])
            else:
                hash = {}
                for pick in range(i,len(nums)):
                    if nums[pick] not in hash:
                        hash[nums[pick]]=1
                        nums[pick],nums[i]=nums[i],nums[pick]
                        helper(nums,i+1)
                        nums[pick], nums[i] = nums[i], nums[pick]
        helper(nums,0)
        return results


'''
Runtime: 60 ms, faster than 77.35% of Python3 online submissions for Permutations II.
Memory Usage: 14.8 MB, less than 17.09% of Python3 online submissions for Permutations II.

'''


# Solution 3 using Python Libraries

from itertools import permutations
def get_permutations(arr):
    # Write your code here
    results = list()
    for i in permutations(arr):
        results.append(i)
    return list(set(results))
