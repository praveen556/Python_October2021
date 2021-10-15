class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mid = length(nums)/2
        for i in range(nums):
            if nums[mid] < target:
                i = mid
                mid += (length(i)-mid)/2
            elif nums[mid] > target:
                i += 1
                mid -= (length(i)-mid)/2
            else:
                return i
