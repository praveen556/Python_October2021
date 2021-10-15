#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

#Example 1:

#Input: nums = [-4,-1,0,3,10]
#Output: [0,1,9,16,100]
#Explanation: After squaring, the array becomes [16,1,0,9,100].
#After sorting, it becomes [0,1,9,16,100].

#Example 2:

#Input: nums = [-7,-3,2,3,11]
#Output: [4,9,9,49,121]


#Constraints:

#1 <= nums.length <= 104
#-104 <= nums[i] <= 104
#nums is sorted in non-decreasing order.


#Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
#Approach 1
class Solution:
    def sortedSquares1(self, nums: list[int]) -> list[int]:
        op = nums
        for i in range(len(nums)):
            op[i] = nums[i]*nums[i]
        op.sort()
        return op

print(Solution.sortedSquares1(1, [-4,-1,0,3,10]))
print(Solution.sortedSquares1(1, [-7,-3,2,3,11]))

#Appraoch 2
class Solution:
    def sortedSquares2(self, nums: list[int]) -> list[int]:
        square = [i*i for i in nums]
        square.sort()
        return square
print(Solution.sortedSquares2(1, [-4,-1,0,3,10]))
print(Solution.sortedSquares2(1, [-7,-3,2,3,11]))


#Approach3
class Solution:
    def sortedSquares3(self, nums: list[int]) -> list[int]:
        return sorted(x*x for x in nums)

print(Solution.sortedSquares3(1, [-4,-1,0,3,10]))
print(Solution.sortedSquares3(1, [-7,-3,2,3,11]))
