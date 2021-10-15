#Add to List

#Share
#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.



#Example 1:

#Input: nums = [1,3,5,6], target = 5
#Output: 2
#Example 2:

#Input: nums = [1,3,5,6], target = 2
#Output: 1
#Example 3:

#Input: nums = [1,3,5,6], target = 7
#Output: 4
#Example 4:

#Input: nums = [1,3,5,6], target = 0
#Output: 0
#Example 5:

#Input: nums = [1], target = 0
#Output: 0
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        Left = 0
        Right = len(nums)-1
        while Left <= Right :
            mid = Left + (Right - Left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                Right = mid - 1
            elif nums[mid] < target:
                Left = mid + 1
        return Left

print("List 5 in [1,3,5,6]")
print(Solution.searchInsert(1,[1,3,5,6],5))

print("List 2 in [1,3,5,6]")
print(Solution.searchInsert(1,[1,3,5,6],2))

print("List 7 in [1,3,5,6]")
print(Solution.searchInsert(1,[1,3,5,6],7))

print("List 0 in [1,3,5,6]")
print(Solution.searchInsert(1,[1,3,5,6],0))

print("List 0 in [1]")
print(Solution.searchInsert(1,[1],0))

print("List 3 in [1,3]")
print(Solution.searchInsert(1,[1,3],3))

print("List 1 in [1]" )
print(Solution.searchInsert(1,[1],1))
