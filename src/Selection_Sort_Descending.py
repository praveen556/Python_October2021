class Sort:
    def Selection(Self, nums: list[int]) -> list[int]:
        length = len(nums)
        for i in range(length-1):
            max_index = i
            for j in range(i+1, length):
                if nums[i]<nums[j]:
                    max_index = j
            nums[max_index], nums[i] = nums[i], nums[max_index]
        return nums

print(Sort.Selection(1,[1,2,3,4,5]))
