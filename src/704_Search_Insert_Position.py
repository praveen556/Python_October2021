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
