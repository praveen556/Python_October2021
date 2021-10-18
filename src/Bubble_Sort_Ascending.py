class Sort:
    def Bubble(self, nums: list[int]) -> list[int]:
        length = len(nums)
        for i in range(length-1):
            for j in range(length-1, i+1, -1):
                if nums[j-1] > nums[j]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
        return nums
print(Sort.Bubble(1,[1,2,4,3,5]))
